import numpy as np

model = {
	"N" : np.zeros( (9,9) )
}

model["N"][1][0] = 1
model["N"][2][0] = 1
model["N"][3][2] = 1
model["N"][4][3] = 1
model["N"][5][3] = 1
model["N"][6][0] = 1
model["N"][7][1] = 1
model["N"][8][4] = 1
model["N"][8][5] = 1
model["N"][8][6] = 1
model["N"][8][7] = 1

print str(model) + "\n"

print model["N"][:,3]