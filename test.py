
def load_optimum(file, it):

	found = False
	fobj = open(file)

	for idx,line in enumerate(fobj):

		strings = line.rstrip().split()

		if len(strings) > 0:

			if found == True and len(strings) > 3:
				if idx == idxObj:
					fobj.close()
					print "ARCHIVO CERRADO"
					return strings[3]	# LB

			if strings[0] == "Par":
				idxObj = idx + it + 2	# 2: 0 index and horizontal line
				found = True

print load_optimum("dataset/j60lb.sm", 82)