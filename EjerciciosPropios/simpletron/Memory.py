class Memory():
    def __init__(self):
        #Este constructor crea un arreglo de 10*10 elementos llenos con 0
        self.memory = [["_"] * 10 for i in range(10)]
        self.buffer = 0
    def getMemory(self):
        #Retorna la memoria
        return self.memory
    def consolePrintMemory(self):
        #imprime las filas de la matris, las cuales son otras matrices reglon
        for i in self.memory:
            print(i)
    def writeInMemory(self,data,i,j):
        #Este metodo cambia un valor de la posicion ij por data
        self.memory[i][j] = data
    def getBuffer(self):
        return self.buffer
    def consolePrintBuffer(self):
        print(self.buffer)
    def changeBuffer(self,data):
        self.buffer = data