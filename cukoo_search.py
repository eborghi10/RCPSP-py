import os
import platform
from functions import *
import SerialSGS

def cuckoo_search(model, T):
	n = 25
	Pa = 0.25

	MaxIt = 400

	sol = CreateRandomSolution(model, n)

	K, sol = getBestNest(sol,sol["Eggs"],model)
	Best = sol

	BestCosts = [0] * MaxIt
	BestCosts[0] = Best["Sol"]["Cmax"]
	it = 0

	while it < MaxIt:
		it += 1

		# Generate new solutions
		newSol["Eggs"] = getCuckoos(sol, K, model)

		# Get the best solution
		None, sol = getBestNest(sol, newSol["Eggs"], model)
		# MPE[it] = 100 * sum()

		# Discover and randomize
		newSol["Eggs"] = empty_nests(sol["Eggs"])

		# Get best solution
		K, newSol = getBestNest(sol, newSol, model)

		if newSol["Sol"]["Cmax"] <= Best["Sol"]["Cmax"]:
			Best["Sol"] = newSol["Sol"]

		BestCosts[it] = Best["Sol"]["Cmax"]

		if MPE[it] == 0:
			break

		sol = newSol

	SerialSGS(model, Best["Sol"]["Sol"], 1)

	return sol, MC, MPE
