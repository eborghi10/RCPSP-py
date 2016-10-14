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

	T = sum(d)				# Upper bound
	ES = np.zeros((1,n))	# Earliest Start Time
	LS = np.zeros((1,n))	# Lastest Start Time

	R = K.shape[0]	# Maximum resource quantity
	Rk = np.tile(K,(1,T))

	S = {
		"Sol" : np.zeros((1,n))
	}

	C = 0

	for mu in range(n):

		D = []

		for dd in ismembc(I,C):
			pass
#			di = 
