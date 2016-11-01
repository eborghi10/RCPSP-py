import numpy as np

def import_from_PSPLIB(file):

	precedence = False
	durations = False
	resources = False

	# DICTIONARY UPDATE OR DEFINE A NEW VARIABLE??

	fobj = open(file)

	for idx,line in enumerate(fobj):

		strings = line.rstrip().split()

		if len(strings) > 1:

			if precedence == True:
				# Creates the precedence matrix
				cnt += 1

				pred = int(strings[2])-1
				for sucs in strings[3:]:
				 	rcpsp['N'][int(sucs)-1][pred] = 1
				
				if cnt == 32:
					precedence = False
					cnt = 0

				# Returns to the top for()
				continue

			elif durations == True:
				# Creates the duration array

				rcpsp['d'][cnt] = strings[2]

				for j in range(1,R):
					rcpsp['r'][j] = strings[2+j]

				cnt += 1

				if cnt == 32:
					durations = False

			elif resources == True:
				# Creates the resource array
				for idx,k in enumerate(strings):
					rcpsp['K'][idx] = k

				fobj.close()
				return rcpsp

			elif strings[0] == "jobs":
				# Number of non-dummy activities
				n = int(strings[4])

				rcpsp = {
					'n' : n-2,
					'N' : np.zeros((n,n)),
					'd' : np.zeros(n),
				}

			elif strings[1] == "renewable":
				# Quantity of resources
				R = int(strings[3])
				rcpsp.update({
					'R' : R,
					'r' : np.zeros((n,R)),
					'K' : np.zeros(R)
				})

			elif strings[1] == "#modes":
				precedence = True
				cnt = 0

			elif strings[1] == "mode":
				durations = True

			elif strings[0] == 'R' and strings[1] == '1':
				resources = True