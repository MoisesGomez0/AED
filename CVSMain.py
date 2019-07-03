#-*- coding: utf-8 -*-
from CVSRandom import *
CSVInstance = CSV()
content = CSVInstance.generateRandomCSV()
print(content)
f = open("csv.csv","w")
f.write(content)
f.close()