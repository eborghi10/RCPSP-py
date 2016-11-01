def use_model(str):

	if len(str) > 0:

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
			raise Exception('Error using model')
	else:
		raise Exception('String of zero length')