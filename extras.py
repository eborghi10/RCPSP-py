import numpy as np

def corregir(s):
	"""
	From the book: "Resource-Constrained Project 
	Scheduling: Models, Algorithms and Applications".
	Chp 1: The Resource Constrained Project Scheduling
	Problem (page 23). Christian ARTIGUES.
	"""
	if s.ndim == 1:
		Ub = s.size
		F = 1
	else:
		F, Ub = s.shape

	# Return indices of sorted 's'
#	I = [i[0] for i in sorted(enumerate(s), \
#		key = lambda x:x[1])]

#	A = np.zeros((F,Ub))

	A = np.tile([i for i in range(1,Ub)],(F,1))

	if A.shape[0] == 1:
		return A[0]
	else:
		return A


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

def checkResources(ES, LS, res, Rk):
#	print "CHECK RESOURCES"
#	raw_input()
	ret = 1
	for t in range(ES,LS):

#		print "t = " + str(t)
#		print "res = " + str(res)
		if res > Rk[0][t]:
			ret = 0
			break

#	print "return: " + str(ret)
	return ret

def buscar(N):
	return [i for i,j in enumerate(N) if j == 1]