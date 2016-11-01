import os
import platform
from CargarModelo import load_model
from metaheuristics import cuckoo_search
from analyze_results import analyze_results
from print_results import print_results
from use_model import use_model

SO = platform.system()

if SO == 'Windows':
	os.system('cls')
elif SO == 'Linux':
	os.system('clear')
else:
	print "ERROR: OS not recognized"

sum_dev = 0
test = "j30"

T = use_model(test)

for it in range(1,T):

	model = load_model(test, it, T)

	sol, MC, MPE = cuckoo_search(model, T)

	analyze_results(model, Sol["Cmax"], it, T, test)

	if T == 1:
		print_results(model, Sol["I"], MC, MPE)