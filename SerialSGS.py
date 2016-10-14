import numpy as np
from extras import *

def SerialSGS(rcpsp, I, graphic):
	# Algorithm: Kolisch [2015] page 9

	I = corregir(I)

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

	C = [0]

	for mu in range(1,n):

		D = []

		print "I = " + str(I)
		print "C = " + str(C)

		print "is not member: " + str(is_not_membc(I,C))

#		raw_input()

		for dd in is_not_membc(I,C):

			# Task in order to be scheduled:
			print "Task to be scheduled = " + str(dd)
#			print "Predecessors = " + str(N[dd+1,:])
			di = buscar(N[dd,:])
			print "Predecessors = " + str(di)

			# All of its predecessor were scheduled?
			if ismembc(di,C):
				D.append(dd)

		print "D = " + str(D)
#		raw_input()
		j = D[0]
		print "Task chosen = " + str(j)

		# Searchs for the Lastest Start Time 
		# of its predecessors
		H = []

		print "Predecessors = " + str(buscar(N[j,:]))

		for h in buscar(N[j,:]):

			print "h = " + str(h)

			if h == 0:
				H.append(0)
			else:
				H.append(S["Sol"][h-1] + d[h])

		print "H = " + str(H)
		print "d = " + str(d)

		ES[j-1] = max(H)
		LS[j-1] = ES[j-1] + d[j]

#		raw_input()

		print "ES = " + str(ES[j-1])
		print "LS = " + str(LS[j-1]-1)
		print "r = " + str(r)
		print "Rk = " + str(Rk)

		while not checkResources(ES[j-1],LS[j-1]-1,r[j],Rk):
			ES[j-1] = ES[j-1] + 1
			LS[j-1] = ES[j-1] + d[j]

		for t in range(ES[j-1],LS[j-1]-1):
			Rk[0][t] += -r[j]

		print "Rk = " + str(Rk[0])
		
#		raw_input()

		S["Sol"][j] = ES[j-1]

		print "S[\"Sol\"] = " + str(S["Sol"])

		C.append(j)

	print "Solucion final: " + str(S["Sol"])

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