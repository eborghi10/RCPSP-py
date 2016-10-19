
def load_optimum(file, it):
	fobj = open(file)

	for line in fobj:
		strings = line.rstrip().split(" ")
		if strings[0] == "Paramter":
			

	fobj.close()

	return opt


print load_optimum("dataset/j30opt.sm", 0)