import numpy as np
from numpy import random as rnd

def CreateRandomSolution(model, n):

	pob = {
		"Eggs" : rnd.rand(n,model["n"]),
		"Fitness" : float('inf') * np.ones(n)
	}

	return pob

def getBestNest(sol, newSol, model):

	for j in sol["Eggs"].shape[0]:

		 = SerialSGS(model, , 0)

		 if 