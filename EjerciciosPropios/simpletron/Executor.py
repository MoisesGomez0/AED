from Memory import *
from Reader import *
class Executor():
    def __init__(self,memory):
        self.memory = memory
    def executor(self):
        #array es la memoria
        array = self.memory.getMemory()
        for i in array:
            for j in i:
                #la instrucción 01 carga la posición adjunta al buffer de la memoria
                if j[:2] == "01":
                    self.memory.buffer = array[int(j[2])][int(j[3])]
                #La instrucción 02 lee un dato de stdin y lo guarda en la posición adjunta
                elif j[:2] == "02":
                    reader = Reader(self.memory)
                    data = reader.inputData()
                    self.memory.writeInMemory(data,int(j[2]),int(j[3]))
                #La instrucción 03 suma lo que esta en el buffer con la posición adjunta 
                # y lo guarda en el buffer
                elif j[:2] == "03":
                    valorSuma = int(array[int(j[2])][int(j[3])])
                    self.memory.buffer =str(int(self.memory.buffer) + valorSuma)
                elif j[:2] == "04":
                    valorResta = int(array[int(j[2])][int(j[3])] )
                    self.memory.buffer =str((self.memory.buffer) - valorResta)
                elif j[:2] == "05":
                    valorProducto = int(array[int(j[2])][int(j[3])])
                    self.memory.buffer =str((self.memory.buffer) * valorProducto)
                elif j[:2] == "06":
                    valorDivisor = int(array[int(j[2])][int(j[3])])
                    try:
                        self.memory.buffer =str((self.memory.buffer) / valorDivisor)
                    except:
                        print("No se pudo ejecutar la operación de que u")
                elif j[:2] == "07":
                    self.memory.writeInMemory("_",int(j[2]),int(j[3]))
                elif j[:2] == "08":
                    print(array[int(j[2])][int(j[3])])
                elif j[:2] == "09":
                    array[int(j[2])][int(j[3])] = str(self.memory.buffer)