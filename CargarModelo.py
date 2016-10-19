from math import abs
import import_from_PSPLIB
from print_graph import print_graph

#def load_optimum():

#def load_limit():

#def load_others():

def load_model(str, it, T):

	# TODO: complete...

	if not str == "[]":
		param = ceil(it/10)
		inst = math.abs(it,10)

		if inst == 0:
			inst = 10

		if str == "j30":
			file = 
		elif str == "j60":
			file = 
		elif str == "j90":
			file = 
		elif str == "j120":
			file =
		else:
			# ERROR loading model

		model = import_from_PSPLIB(file)

		if str == "j30":
			file = 
			model.update({
				"Opt" : load_optimum(file, it)
				"instances" : inst
				})
		else:
			# ERROR loading model

	else:
		model = load_others()

	if T == 1:
		levels = print_graph(model)

	return model