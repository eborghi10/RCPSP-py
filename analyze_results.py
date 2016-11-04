def analyze_results(model, cmax, it, T, test):

	global sumDev

	if model["Opt"] and model["instances"]:
		# If they are not empty
		opt = model["Opt"]

		# s: best solution found
		dev_i = (cmax - opt) / opt
		print "* DEVi = " + str(dev_i) + "\t MC(" \
			+ str(it) + ")=" + str(cmax)

		if cmax < opt:
			print "BEST SOLUTION (" + str(it) + ")!!!"

		if it < T:
			sumDev += dev_i
		else:
			if test == "j30":
				dev_avg = (sumDev + dev_i) / 480
			elif test == "j60":
				dev_avg = (sumDev + dev_i) / 450
			elif test == "j90":
				dev_avg = (sumDev + dev_i) / 445
			elif test == "j120":
				dev_avg = (sumDev + dev_i) / 600
			else:
				print "PSPLIB not found."
				dev_avg = '-'
			
			print "* DEVavg = " + str(dev_avg)
	else:
		print "* The analized model didn't belong to PSPLIB"