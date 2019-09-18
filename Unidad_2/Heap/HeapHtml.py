from LinkedListForHeap import *
import math

class Heap:
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist
        self.n = None
        self.w = None
        self.mi = None
        self.mf = None
        self.h = None

    def setSizes(self,n):
        if n>self.linkedlist.count():
            return False
        else:
            self.n = n
            self.h = math.ceil(math.log2(n+1))
            self.mi = 2**(self.h-1)-1
            self.mf = 2*self.mi
            self.w = self.mf+1

    def makeHtml(self):
        html = []
        firstPost = self.w//2
        spaces = firstPost
        lastPost = -1500
        index = 0
        cant = 0
        html.append("<table align='center'>")
        for i in range(self.h):
            html.append("<tr>")
            for j in range(self.w):
                if j == firstPost:
                    html.append("<td>%s</td>"%self.linkedlist.getValueIndex(index))
                    index += 1
                    cant += 1
                elif (j == firstPost+spaces+1 or lastPost+spaces+1 == j) and cant <= 2**i and index<self.n:
                    lastPost = j
                    html.append("<td>%s</td>"%self.linkedlist.getValueIndex(index))
                    index += 1
                    cant +=1
                else:
                    html.append("<td>&nbsp</td>")
            html.append("</tr>")
            spaces = firstPost
            firstPost = firstPost//2
            cant = 0
        html.append("</table")
        return "".join(html)


lista = LinkedList()
lista.add(2)            
lista.add("4gf")            
lista.add("#")            
lista.add(6543)            
lista.add("345")            
lista.add("DF")            
lista.add("GFDS55")            
lista.add("dfg")            
lista.add(434)            
lista.add("fddfg")


arbol = Heap(lista)
arbol.setSizes(5)
f = open("TableFromHeap.html","w")
f.write(arbol.makeHtml())
f.close()