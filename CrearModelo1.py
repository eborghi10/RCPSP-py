import numpy as np

# Crear un modelo de RCPSP de un recurso

def create_model():
	
	Modelo = {
	"R" : 1,
	"r" : [0, 2, 6, 4, 4, 3, 1, 5, 0],
	"d" : [0, 4, 2, 1, 4, 4, 5, 3, 0]
	}

	L = len(Modelo["r"])

	Modelo.update( {
		"K" : 6,
		"n" : L - 2,
		"N" : np.zeros( (L,L) )
	} )

	Modelo["N"][1][0] = 1
	Modelo["N"][2][0] = 1
	Modelo["N"][3][2] = 1
	Modelo["N"][4][3] = 1
	Modelo["N"][5][3] = 1
	Modelo["N"][6][0] = 1
	Modelo["N"][7][1] = 1
	Modelo["N"][8][4] = 1
	Modelo["N"][8][5] = 1
	Modelo["N"][8][6] = 1
	Modelo["N"][8][7] = 1

	return Modelo