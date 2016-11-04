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

	p, j = LevyFlights(F)
	Q = q[j]
	N = model["N"]

	if p >= 0 and p <= 0.3:
		qNew = Insertion(Q,N)
	elif p > 0.3 and p <= 1:
		qNew = Swap(Q,N)
	else :
		raise Exception('Error generating a new solution')

	# Convierte a la tarea en viable
	x = SSGS(model, qNew, 0)
	qNew = x["Sol"]


def Swap(Q, N):

	from extras import buscar, get_limits, search_index

	# Selects the task to swap
	i = rnd.randint(1, max(Q)+1)
	idxI = buscar(Q == i)
	pred, sucs = get_limits(N, i, Q)
	idxPos = search_index(pred.pop(), sucs.pop(), Q)
	# NOTE: Swap() doesn't generate infeasible solutions
	Q[idxI], Q[idxPos] = Q[idxPos], Q[idxI]

	return Q


def Insertion(Q, N):

	from extras import buscar, get_limits, search_index
	
	# Selects the task to insert
	i = rnd.randint(1, max(Q)+1)
	idxI = buscar(Q == i)
	pred, sucs = get_limits(N, i, Q)
	idxPos = search_index(pred.pop(), sucs.pop(), Q)
	# NOTE: Insertion() doesn't generate infeasible solutions
	np.insert(Q, idxPos, idxI)

	return Q


def LevyFlights(Fitness):
	
	from metaheuristics import n
	import math

	alpha = 1.5
	s = 5.9
	j = rnd.randint(1, n)
	F = Fitness[j]

	u = F - min(Fitness)
	v = max(Fitness) - min(Fitness)

	if v == 0:
		step_size = 0
	else :
		u = u / v
		step_size = math.exp(-s * (u ** alpha))

	return step_size, j