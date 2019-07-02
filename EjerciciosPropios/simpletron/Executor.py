from Memory import *
from Reader import *
class Executor():
    def __init__(self,memory):
        self.memory = memory
    def executor(self):
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