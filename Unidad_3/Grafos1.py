#-*- coding:utf8 -*-
"""
En este ejemplo vamos a hacer un TDA de tipo grafo no digirido
""" 
import copy
class Graph:
    def __init__(self,json):
        self.json:dict = json
    def edges(self,vertex):
        s:dict={}
        for k,v in self.json.items():
            if k==vertex:
                for i in v:
                    s[i]=None
            elif vertex in v:
                s[k]=None
        return list(s.keys())
    def isWayFromTo(self,start,end):
        if end in self.json[start]:
            return True
        for i in self.json[start]:
            if self.isWayFromTo(i,end):
                return True
        return False
    def waysTo(self,start,end):
        ways = []
        way = []
        if not self.isWayFromTo(start,end):
            return []
        else:
            if end in self.json[start]:
                way.append(start)
                way.append(end)
                ways.append(copy.copy(way))
                way.clear()
            for i in self.json[start]:
                if self.isWayFromTo(i,end):
                    way.append(i)
                    self.waysTo(i,end,ways,way)
            return ways
grafo = {
    "A":["B","C","E"],
    "B":["A","c","D","E"],
    "C":["A","B","E"],
    "D":["B"],
    "E":["A","C"]
}

G = Graph(grafo)
print(G.isWayFromTo("A","E"))
print(G.waysTo("A","E"))