import networkx as nx 
import matplotlib.pyplot as plt

G = nx.DiGraph()

grafo = {
    "A":["B","C"],
    "B":["C","D"],
    "C":[],
    "D":[]
}

for vertice, aristas in grafo.items():
    G.add_node("%s" % vertice)
    for arista in aristas:
        G.add_node("%s" % arista)
        G.add_edge("%s" % vertice,"%s" % arista,weigth=1)
nx.draw_circular(G,with_labels=True)
plt.savefig("GrafoDirigido.png")
plt.show()
