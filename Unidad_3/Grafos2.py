# -*- coding:utf8 -*-
class GraphDir:
    def __init__(self):
        self.json = {}

    def addVertex(self, name):
        self.json[name] = []

    def addEdge(self, vertexOrigin, vertexDestination):
        if not vertexDestination in self.json[vertexOrigin]:
            self.json[vertexOrigin].append(vertexDestination)

    def __str__(self):
        return str(self.json)


class NoDirGraph:
    def __init__(self):
        self.json = {}
    def __str__(self):
        return str(self.json)

    def addVertex(self, name):
        if not name in self.json.keys():
            self.json[name] = []

    def addEdge(self, vertex1, vertex2):
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        if not vertex2 in self.json[vertex1]:
            self.json[vertex1].append(vertex2)
        if not vertex1 in self.json[vertex2]:
            self.json[vertex2].append(vertex1)
    def __str__(self):
        return str(self.json)
G = NoDirGraph()
G.addVertex("A")
G.addVertex("B")
G.addVertex("C")
G.addVertex("D")
G.addVertex("E")
G.addVertex("F")
G.addEdge("A", "B")
G.addEdge("D","G")
G.addEdge("A","G")
print(G)
