def corregir(s):
	"""
	From the book: "Resource-Constrained Project 
	Scheduling: Models, Algorithms and Applications".
	Chp 1: The Resource Constrained Project Scheduling
	Problem (page 23). Christian ARTIGUES.
	"""
	print "CORREGIR = " + str(s)
	F, Ub = s.shape

	# Return indices of sorted 's'
#	I = [i[0] for i in sorted(enumerate(s), \
#		key = lambda x:x[1])]

#	A = np.zeros((F,Ub))

	return np.tile([i for i in range(Ub)],(F,1))


def ismember2(a, b):
    membs = []
    for elmt in b:
    	if (elmt not in membs) and (elmt in a):
    		membs.append(elmt)
    return membs

def ismember(a, b):
    
    return [1 if itm in b else 0 for itm in a]

def ismember3(a,b):

	return [itm if itm in b else 0 for itm in a]

def ismembc(a,b):

	return [itm for itm in a if itm in b]