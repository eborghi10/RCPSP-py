import numpy as np
from numpy import random as rnd
from SerialSGS import SerialSGS as SSGS

def CreateRandomSolution(model, n):

	pob = {
		"Eggs" : rnd.rand(n,model["n"]),
		"Fitness" : [float('inf')] * n
	}

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
