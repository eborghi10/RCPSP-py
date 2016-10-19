# Make a graph on screen

#import networkx as nx
#import matplotlib.pyplot as plt
import graphviz as gv
from PIL import Image

def print_graph(rcpsp):

# http://matthiaseisen.com/articles/graphviz/

	n = rcpsp["n"]
	N = rcpsp["N"]

	# Create graph
	G = gv.Digraph(format='jpg')
#	G = gv.Graph(format='svg')

	# Create nodes for GraphViz
	for node in range(n+2):
		G.node(str(node+1))

	# Add edges
	graph = [(i+1,j+1) for i in range(n+2) for j,itm in enumerate(N[:][i]) if itm == 1.0]
	
	for edge in graph:
		G.edge(str(edge[1]),str(edge[0]))

	# Save to file and show it
	G.render(filename='img/graph')
	img = Image.open('img/graph.jpg')
	img.show()

	levels = 0
	return levels