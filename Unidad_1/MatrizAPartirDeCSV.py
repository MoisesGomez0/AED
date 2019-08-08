file = open("Archivo.csv","r")
contend = file.read()
rows = contend.split("\n")
matrix = []
for row in rows:
    columns = row.split(",")
    matrix.append(columns)
for i in matrix:
    print(i)