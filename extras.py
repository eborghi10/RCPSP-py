import numpy as np

def srk2al(s):
	"""
	From the book: "Resource-Constrained Project 
	Scheduling: Models, Algorithms and Applications".
	Chp 1: The Resource Constrained Project Scheduling
	Problem (page 23). Christian ARTIGUES.
	"""

	'''
	if s.ndim == 1:
		Ub = s.size
		F = 1
	else:
		F, Ub = s.shape
		# TODO:---
	'''
	# Return indices of sorted 's'
# TODO: THIS IS NOT THE CORRECT IMPLEMENTATION!!
# Correct example:
# s = [0.3989, 0.8145, 0.1769, 0.2486, 0.9397, 0.9713, 0.1771]
# return -> [4 5 1 3 6 7 2]
	return np.argsort(s)


def ismember2(a, b):
    membs = []
    for idx, elmt in enumerate(b):
    	if (elmt not in membs) and (elmt in a):
    		membs.append(idx)
    return membs

def ismember(a, b):
    
    return [1 if itm in b else 0 for itm in a]

def ismember3(a,b):

	return [itm if itm in b else 0 for itm in a]

def ismembc(a,b):

	return [itm for itm in a if itm in b]

def is_not_membc(a,b):

	return [itm for itm in a if itm not in b]

def A(C, t, sol, rcpsp):
	s = 0
	r = rcpsp["r"]
	d = rcpsp["d"]

	for c in C:
		if c:
			if (sol[c] <= t) and (sol[c]+d[c+1] > t):
				s += r[c+1]
	return s

def checkResources(ES, d, res, Rk):

	dur = ES + d
	n = 0

#	print "ES: " + str(ES) + "\t LS: " + str(dur)
#	print ""
#	print "Rk = " + str(Rk[0][:])
#	print "res = " + str(res)
#	raw_input()
	
# TODO: FUNCIONA SOLO PARA UN SOLO RECURSO
	
#	V = np.tile(res, d)
#	print "V = " + str(V)
#	R = Rk[0][ES+n:dur+n]
#	print "Rk = " + str(R)
#	raw_input()
#	cond = V > R
#	print "cond -> " + str(cond) + " -> " + str(any(cond))
#	raw_input()

	while any(np.tile(res, d) > Rk[0][ES+n:dur+n]):
		n += 1
#		V = np.tile(res, d)
#		R = Rk[0][ES+n:dur+n]
#		print str(V) + " > " + str(R)

	ES += n

	return ES, ES+d


def buscar(N):
	return [i+1 for i,j in enumerate(N) if j == 1]


def MPE(F, C):

	return 100 * sum((F-C)/F) / nSol


def meanRUR(rcpsp, res, C):
	
	mean(RUR(rcpsp, res, C))


def get_limits(N, i, Q) :
	# Calculates the indices of the predecessor and successor
	# N: Precedence matrix
	# i: Task

	## Predecessors

	# Substract each element
#	_pred_ = [x - 1 for x in buscar(N[i-1])]
	_pred_ = buscar(N[i-1])

	if len(_pred_) > 1 :
		# If there is more than one predecessor,
		# I have to choose who the tardiness start
		V = buscar(Q==_pred_[1])
		pred = _pred_[1]
		for a in pred[2:]:
			Vp = buscar(Q==a)
			if Vp > V:
				V = Vp
				pred = a
	else :
		pred = _pred_

	## Successors
#	_sucs_ = [x -1 for x in buscar(N[:][i-1])]
	_sucs_ = buscar(N[:,i-1])

	if len(_sucs_) > 1 :
		# If there is more than one successor,
		# I have to choose which starts first
		V = buscar(Q==_sucs_[1])
		sucs = _sucs_[1]
		for a in _sucs_[2:]:
			Vp = buscar(Q==a)
			if Vp < V :
				V = Vp
				sucs = a
	else :
		sucs = _sucs_

	return pred, sucs

def search_index(pred, sucs, Q) :
	print "search_index():"
	print "Q: " + str(Q)
	print "pred: " + str(pred)
	print "sucs: " + str(sucs)

	n = len(Q) # Number of non-dummy tasks

	if pred == 1 and sucs == n+2 :
		# The task can be moved to any position
		pos = np.random.randint(2, n+2)
	elif pred == 1 :
		# There is no left limit
		pos = np.random.randint(2, sucs)
	elif sucs == n+2 :
		# There is no right limit
		pos = np.random.randint(pred, n+2)
	else :
		# There is no problem with the limits
		pos = np.random.randint(pred, sucs)

	asd =  buscar(Q==pos)
	raw_input()
	print "asd=" + str(asd)
	return asd