#-*- coding:utf8 -*-
import networkx as nx 
import matplotlib.pyplot as plt

G = nx.Graph()

grafo = {
    "A":["B","C","E"],
    "B":["A","c","D"],
    "C":["A","B","E"],
    "D":["B"],
    "E":["A","C"]
}
for vertice, aristas in grafo.items():
    G.add_node("%s" % vertice)
    for arista in aristas:
        G.add_node("%s" % arista)
        G.add_edge("%s" % vertice, "%s" %arista, weight = 1)
nx.draw(G,with_labels=True)
plt.savefig("GrafoNoDirigido.png")
plt.show()