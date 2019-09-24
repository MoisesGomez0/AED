import networkx as nx
import matplotlib.pyplot as plt


class NoDirGraph:
    def __init__(self):
        self.json = {}
        self.fig = nx.Graph()

    def __str__(self):
        return str(self.json)

    def addVertex(self, name):
        if name not in self.json.keys():
            self.json[name] = []

    def addEdge(self, vertex1, vertex2):
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        if vertex2 not in self.json[vertex1]:
            self.json[vertex1].append(vertex2)
        if vertex1 not in self.json[vertex2]:
            self.json[vertex2].append(vertex1)

    def showDraw(self):
        for vertice, aristas in self.json.items():
            self.fig.add_node("%s" % vertice)
            for arista in aristas:
                self.fig.add_node("%s" % arista)
                self.fig.add_edge("%s" % vertice, "%s" % arista, weight=1)

        labels={(vertex1,vertex2): weigth["weight"] for vertex1,vertex2,weigth in self.fig.edges(data=True)}
        nx.draw_circular(self.fig, with_labels=True)
        plt.show()
    
    def isconnected(self,initialVertex,finalVertex):
        if finalVertex in self.json[initialVertex]:
            return True
        for i in self.json[initialVertex]:
            if self.isconnected(i,finalVertex):
                return True
        return False

    def getRoads(self,initialVertex,finalVertex,json,road=None,roads=None,searching=[]):
        print(roads)
        if not roads:
            for i in json:
                if initialVertex in json[i]:
                    json[i].remove(initialVertex)
            road = []
            roads = []

        if not initialVertex in road:
            road.append(initialVertex)

        if finalVertex in json[initialVertex]:
            json[initialVertex].remove(finalVertex)
            road.append(finalVertex)
            if road in roads:
                return roads
            roads.append(road.copy())
            road.clear()

        if not initialVertex in road:
            road.append(initialVertex)

        for i in json[initialVertex]:
            if self.isconnected(i,finalVertex):
                self.getRoads(i,finalVertex,json,road,roads)
                json[initialVertex].remove(i)      


g = NoDirGraph()
g.addEdge("A","B")
g.addEdge("A","C")
g.addEdge("A","E")
g.addEdge("B","C")
g.addEdge("B","D")
g.addEdge("B","E")
g.addEdge("C","E")
g.addEdge("D","B")
g.getRoads("A","E",g.json)