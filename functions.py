import numpy as np
from numpy import random as rnd
from SerialSGS import SerialSGS as SSGS

def CreateRandomSolution(model, sol='RandomKey'):

	from metaheuristics import n

	nAct = model["n"]

	if sol == "ActivityList":
	
		pob = {
			"Eggs" : np.zeros((n,nAct))
		}

		for i in range(n):
			pob["Eggs"][i] = rnd.permutation(nAct)
	
	elif sol == "RandomKey":

		pob = {
			"Eggs" : rnd.rand(n,nAct)
		}

	else:
		raise Exception('Error generating new random solutions')

#	"Fitness" : [float('inf')] * n

	pob.update({
		"Fitness" : np.zeros(n)
	})

	for i in range(n):
		# Convierte a las tareas en viables
		x = SSGS(model, pob["Eggs"][i],0)
		pob["Eggs"][i] = x["Sol"]
		pob["Fitness"][i] = x["Cmax"]

	return pob

def getBestNest(sol, newEgg, model):

	for j in range(sol["Eggs"].shape[0]):

		newSol = SSGS(model, sol["Eggs"][j] , 0)
		
		if newSol["Cmax"] <= sol["Fitness"][j]:
			sol["Fitness"][j] = newSol["Cmax"]
			sol["Eggs"][j] = newEgg[j]

	K = sol["Fitness"].index(min(sol["Fitness"]))
	
	sol.update({
		"sol" : SSGS(model, sol["Eggs"][K],0)
	})

	return K, sol


def getCuckoos(model, pob):

	q = pob["Eggs"]
	F = pob["Fitness"]
	N = model["N"]

	p, j = LevyFlights(F)
	Q = q[j]	

	print "q[" + str(j) + "] = " + str(Q)
	raw_input()

	if p >= 0 and p <= 0.3:
		qNew = Insertion(Q,N)
	elif p > 0.3 and p <= 1:
		qNew = Swap(Q,N)
	else :
		raise Exception('Error generating a new solution')

	# Convierte a la tarea en viable
	x = SSGS(model, qNew, 0)
	return x["Sol"]


# TODO: Swap() e Insertion() son funciones bastante similares

def Swap(Q, N):

# TODO: There are some common lines between Swap() and Insertion(),
#		they can be placed in a common function to avoid duplicates.
	
	from extras import buscar, get_limits, search_index

	# Selects the task to swap
	i = rnd.randint(2, max(Q)+1)	# Choose a non-dummy task [2;n)
	idxI = buscar(Q == i)

	print "Swap: j=" + str(i)
	print "Q_0 = " + str(Q)
	pred, sucs = get_limits(N, i, Q)

	idxPos = search_index(pred.pop(), sucs.pop(), Q)
	# NOTE: Swap() doesn't generate infeasible solutions
	print "[" + str(idxI) + "] <-> [" + str(idxPos) + "]"
	Q[idxI], Q[idxPos] = Q[idxPos], Q[idxI]
	print "Q_1 = " + str(Q)
	return Q


def Insertion(Q, N):

	from extras import buscar, get_limits, search_index

	# Selects the task to insert
	i = rnd.randint(2, max(Q)+1)	# Choose a non-dummy task [2;n)
	idxI = buscar(Q == i)

	print "Insertion: j=" + str(i) + "\t[idxI] = " + str(idxI)
	print "Q_0 = " + str(Q)
	pred, sucs = get_limits(N, i, Q)

	idxPos = search_index(pred.pop(), sucs.pop(), Q)
	# NOTE: Insertion() doesn't generate infeasible solutions
	print "[" + str(idxPos) + "] -> [" + str(idxI) + "]"
	np.insert(Q, idxPos, idxI)
	print "Q_1 = " + str(Q)
	return Q


def LevyFlights(Fitness):
	
	from metaheuristics import n
	import math

	alpha = 1.5
	s = 5.9
	j = rnd.randint(0, n)
	F = Fitness[j]

	u = F - min(Fitness)
	v = max(Fitness) - min(Fitness)

	if v == 0:
		step_size = 0
	else :
		u = u / v
		step_size = math.exp(-s * (u ** alpha))

	return step_size, j


def mutation(q,K,F,N):

	from extras import get_limits

	n = len(q[0])
	qNew = np.zeros(q.shape)
	f = min(F)
	for j in range(1, q.shape[1]+1):
	# To do the mutation, the task MUST BE DISCOVERED and
	# NOT BE the BEST.
	    if K[j] and (not F[j] == f):
	        # Select the number of tasks to swap
	        M = np.randint(n);
	        for m in range(1,M+1):
	            # Select the task to swap
	            Q = q[j]
	            i = np.randint( max(Q) )
	            idxI = buscar(Q == i)
	            [Pred,Sucs] = get_limits(N,i,Q);
	            idxPos = search_index(Pred,Sucs,Q);
				# NOTA: Esta operacion no genera soluciones inviables
	            if idxPos > idxI:
	                qNew[j] = [
	                			q[j][:idxI-1], 
	                			q[j][idxPos],
	                    		q[j][idxI+1:idxPos-1], 
	                    		q[j][idxI], 
	                    		q[j][idxPos+1:]
	                		]
	            elif idxPos < idxI:
	                qNew[j] = [
	                			q[j][:idxPos-1],
	                			q[j][idxI],
	                			q[j][idxPos+1:idxI-1],
	                			q[j][idxPos],
	                			q[j][idxI+1:]
	                		]
	            else:
	                qNew[j] = q[j]
	    else:
	        qNew[j] = q[j]

	return qNew


def empty_nests(pob, rcpsp):

	from metaheuristics import n, Pa

	q = pob["Eggs"]
	F = pob["Fitness"]
	N = rcpsp["N"]
	# The eggs are discovered and are replaced by new ones with a 
	# probability 'Pa'.
	
	# 'K' indicates which eggs are discovered
	# rnd.random.rand(nSol, 1) > Pa

	K = [1 if itm > Pa else 0 for itm in np.random.rand(n)]

	new_nest = {
    	"Eggs" : mutation(q,K,F,N),
    	"Fitness" : pob["Fitness"]
    }

	for j in range(1,n+1):
		if K(j):
			new_nest["Fitness"][j] = MakeSpan(rcpsp,new_nest["Eggs"][j])