import os
import platform
from CrearModelo import CrearModelo
from functions import *

SO = platform.system()

if SO == 'Windows':
	os.system('cls')
elif SO == 'Linux':
	os.system('clear')
else:
	print "ERROR: OS not recognized"

model = CrearModelo()

n = 25
Pa = 0.25

MaxIt = 400

sol = CreateRandomSolution(model, n)

K, sol = getBestNest(sol,sol["Eggs"],model)
Best = sol

BestCosts = [0] * MaxIt
