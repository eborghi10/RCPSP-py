import os
import platform
from CargarModelo import load_model
import cuckoo_search
import analyze_results
import print_results

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

for it in range(T):

	model = load_model(test, it, T)

	sol, MC, MPE = cukoo_search(model, T)

	analyze_results(model, Sol["Cmax"], it, T, test)

	if T == 1:
		print_results(model, Sol["I"], MC, MPE)

# fclose(All)