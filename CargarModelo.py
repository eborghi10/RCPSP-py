from math import ceil
from PSPLIB import import_from_PSPLIB
from print_graph import print_graph

def load_optimum(file, it):

	found = False
	fobj = open(file)

	for idx,line in enumerate(fobj):

		strings = line.rstrip().split()

		if found == True and len(strings) > 3:
			if idx == idxObj:
				fobj.close()
				return strings[2]

		if strings[0] == "Paramter":
			idxObj = idx + it + 2	# 2: 0 index and horizontal line
			found = True

def load_limit(file, it):

	found = False
	fobj = open(file)

	for idx,line in enumerate(fobj):

		strings = line.rstrip().split()

		if len(strings) > 0:

			if found == True and len(strings) > 3:
				if idx == idxObj:
					fobj.close()
					return strings[3]	# LB

			if strings[0] == "Par":
				idxObj = idx + it + 2	# 2: 0 index and horizontal line
				found = True

def load_others():

	from CrearModelo1 import create_model

	model = create_model()
	model["opt"] = []
	model["instances"] = []

#	model = import_from_PSPLIB("Tests/j30/j301_1.sm")
#	model["opt"] = 43
#	model["instances"] = 1

#	model = import_from_PSPLIB("Tests/j120/j1205_8.sm")
#	model["opt"] = 78
#	model["instances"] = 8

	return model


def load_model(string, it, T):

	if not string == "[]":
		param = int(ceil(it/10.0))
		inst = it%10

		if inst == 0:
			inst = 10

		if string == "j30":
			file = "tests/j30/j30" + str(param) \
				+ "_" + str(inst) + ".sm"
		elif string == "j60":
			file = "tests/j60/j60" + str(param) \
				+ "_" + str(inst) + ".sm"
		elif string == "j90":
			file = "tests/j90/j90" + str(param) \
				+ "_" + str(inst) + ".sm"
		elif string == "j120":
			file = "tests/j120/j120" + str(param) \
				+ "_" + str(inst) + ".sm"
		else:
			raise Exception('Error loading model')

		model = import_from_PSPLIB(file)

		if string == "j30":
			file = "dataset/j30opt.sm"
			model.update({
				"Opt" : load_optimum(file, it),
				"instances" : inst
			})
		elif string == "j60":
			file = "dataset/j60lb.sm"
			model.update({
				"Opt" : load_limit(file, it),
				"instances" : inst
			})
		elif string == "j90":
			file = "dataset/j90lb.sm"
			model.update({
				"Opt" : load_limit(file, it),
				"instances" : inst
			})
		elif string == "j120":
			file = "dataset/j120lb.sm"
			model.update({
				"Opt" : load_limit(file, it),
				"instances" : inst
			})
		else:
			raise Exception('Error loading model')

	else:
		model = load_others()

	if T == 1:
		levels = print_graph(model)

	return model