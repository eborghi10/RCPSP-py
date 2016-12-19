# coding=utf-8

import os
import platform
from functions import *
from SerialSGS import SerialSGS, makespan
from numpy import random as np

def cuckoo_search(model, T):

	global n, Pa

	n = 25
	Pa = 0.25

	MaxIt = 400

	pob = CreateRandomSolution(model, 'ActivityList')
#	pob = CreateRandomSolution(model, 'RandomKey')

	BestCosts = [0] * MaxIt
	MPE = [0] * MaxIt
	it = 0

	while it < MaxIt :

		it += 1

		# Generate new solutions
		newEgg = getCuckoos(model, pob)

		# Calculate Makespan
		cmax, Rk = makespan(model, newEgg)

		j = np.randint(1,n)
		Fj = pob["Fitness"][j]

		if cmax < Fj:
			# Evito el cálculo innecesario de RUR()
			pob["Fitness"][j] = cmax
			pob["Eggs"][j] = newEgg
		elif cmax == Fj:
			_, Rj = makespan(model, pob["Eggs"][j])
			if meanRUR(model, Rk, cmax) < meanRUR(model, Rj, Fj):
				Pob["Fitness"][j] = cmax
				Pob["Eggs"][j] = newEgg

		# Discover and randomize
		pob = empty_nests(pob, model)

		# Get the best solution
		_, pob = getBestNest(pob, newPob["Eggs"], model)
		MPE[it] = MPE(pob["Fitness"], cmax)
		BestCosts[it] = cmax

		Sol["I"] = pob["Eggs"][j]
		Sol["Cmax"] = cmax

		if T == 1:
			print str(it) + " :: Best Cost = " + str(BestCosts[it])

		if MPE[it] == 0:
			break

	return pob, BestCosts[:it], MPE[:it]