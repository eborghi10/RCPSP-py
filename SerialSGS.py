import numpy as np
from extras import *

def newTask(D, i, string):
	# Selects the best task to be scheduled
	#
	# Priority Rule-Based Heuristics
	# "Handbook of Recent Advances in Scheduling" - Kolisch [1999]
	# " HEURISTIC ALGORITHMS FOR SOLVING THE RESOURCE-CONSTRAINED PROJECT
	# SCHEDULING PROBLEM: CLASSIFICATION AND COMPUTATIONAL ANALYSIS"
	if string == "FIFO":
		j = D[0]
		D.remove(D[0])
	elif string == "FIFOenI":
		# TODO: COMPLETE
		j = j[0]
		#
	else:
		j = D[0]
		D.remove(D[0])

	return j, D

def makespan(rcpsp, I):

	# TODO.
	pass

def SerialSGS(rcpsp, I, graphic):
	# Algorithm: Kolisch [2015] page 9

	I = srk2al(I) + 2

	n = rcpsp["n"]	# Number of non-dummy activities
	d = rcpsp["d"]	# Processing time of each activity
	K = rcpsp["K"]	# Maximum stock quantity for ea. resource
	r = rcpsp["r"]	# Resource consumption of each task
	N = rcpsp["N"]	# Precedence constraints

	T = sum(d)		# Upper bound
	ES = [0] * n	# Earliest Start Time
	LS = [0] * n	# Lastest Start Time

	R = K	# Maximum resource quantity
	Rk = np.tile(K,(1,T))

	S = {
		"Sol" : [0] * n
	}

	C = [1]

	for mu in range(1,n+1):

		D = []

#		print "I = " + str(I)
#		print "d = " + str(d[1:-1])
#		print "C = " + str(C)
#		print "dd = " + str(is_not_membc(I,C))
		
		for dd in is_not_membc(I,C):

			# Task in order to be scheduled:
			di = buscar(N[dd-1,:])
#			print "Task to be scheduled = " + str(dd) \
#				+ "\t Predecessors = " + str(di)
#			raw_input()

			# All of its predecessor were scheduled?
			if ismembc(di,C):
				D.append(dd)

#		print "D = " + str(D)
		j = D[0]
#		print "Task chosen = " + str(j) + "\td = " + str(d[j-1]) + "\n"

		# Searchs for the Lastest Start Time 
		# of its predecessors
		H = []

		for h in buscar(N[j-1,:]):

#			print "h = " + str(h)

			if h == 1:
				H.append(0)
			else:
				H.append(S["Sol"][h-1] + d[h-1])

#		print "H = " + str(H)
#		print "d_j = " + str(d[j-1]) + "\t (int) = " + str(int(d[j-1]))

		ES[j-2] = int(max(H))
		LS[j-2] = ES[j-2] + int(d[j-1])

#		print "ES: " + str(ES) + "\t LS: " + str(LS)

		ES[j-2], LS[j-2] = checkResources(ES[j-2],d[j-1],r[j],Rk)

#		print "ES: " + str(ES) + "\t LS: " + str(LS) + "\n"

# TODO: PONER DENTRO DE CheckResources()
		for t in range(ES[j-2],LS[j-2]):
			Rk[0][t] += -r[j]

		S["Sol"][j-2] = ES[j-2]

		C.append(j)

#	print "Solucion final: " + str(S["Sol"])

	ind = S["Sol"].index(max(S["Sol"]))

	S.update({
		"Cmax" : LS[ind]
	})

	Z = {
		"Sol" : I,
		"Cmax" : S["Cmax"],
		"Rk" : Rk
	}	

	return Z
