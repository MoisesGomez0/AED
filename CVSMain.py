#-*- coding: utf-8 -*-
""" 
    crear un programa en python que genere un contenido CSV. con un número de filas aleatorio
    donde cada fila tiene columas aleatorias. use TDA's

"""
from CVSRandom import *
CSVInstance = CSV()
content = CSVInstance.generateRandomCSV()
print(content)
f = open("csv.csv","w")
f.write(content)
f.close()