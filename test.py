def srk2al(s):

	print "s: " + str(s)

	A = [i[0] for i in sorted(enumerate(s), key=lambda x:x[1])]

	print "A: " + str(A)
	return A

srk2al([0.3989, 0.8145, 0.1769, 0.2486, 0.9397, 0.9713, 0.1771])

# A = [4 5 1 3 6 7 2];

