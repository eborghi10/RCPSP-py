def use_model(str):

# TODO: check argument

	if str == "j30":
		return 480
	elif str == "j60":
		return 450
	elif str == "j90":
		return 445
	elif str == "j120":
		return 600
	elif str == "[]":
		return 1
	else:
# TODO: print errors in Python
		print "# ERROR Using model of a task #"