"""
Para representar un grafo en JSON cada vértice será un índice y cada arista 
sera un elemento en un arreglo de vertices como el valor de índice.
"""
#Este grafo es el que esta en la imagen GrafoDirigido.png
grafo = {
    "A":["B","C"],
    "B":["c","D"],
    "C":[],
    "D":[]
}

#Este grafo esta en la imagen GrafoNoDirigido.png
grafo = {
    "A":["B","C","E"],
    "B":["A","c","D"],
    "C":["A","B","E"],
    "D":["B"],
    "E":["A","C"]
}
