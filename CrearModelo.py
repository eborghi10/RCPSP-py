import numpy as np

# Crear un modelo de RCPSP de un recurso

def CrearModelo():
	Modelo = {
	"R" : 1,
	"r" : [0, 2, 6, 4, 4, 3, 1, 5, 0],
	"d" : [0, 4, 2, 1, 4, 4, 5, 3, 0]
	}

	L = len(Modelo["r"])

	Modelo.update( {
		"K" : 6,
		"n" : L - 2,
		"N" : np.zeros( (L+2,L+2) )
	} )

	Modelo["N"][2][1] = 1
	Modelo["N"][3][1] = 1
	Modelo["N"][4][3] = 1
	Modelo["N"][5][4] = 1
	Modelo["N"][6][4] = 1
	Modelo["N"][7][1] = 1
	Modelo["N"][8][2] = 1
	Modelo["N"][9][5] = 1
	Modelo["N"][9][6] = 1
	Modelo["N"][9][7] = 1
	Modelo["N"][9][8] = 1

	return Modelo