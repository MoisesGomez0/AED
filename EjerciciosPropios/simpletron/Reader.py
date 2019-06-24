class Reader():
    def __init__(self,memory):
        self.memory = memory

    def inputInstruction(self,count_i,count_j):
        value = input("Escribe la instruccion que se guarda en la posicion ["+str(count_i)+"]["+str(count_j)+"]: ")
        if len(value) < 3 and value !="-1":
            print("La instruccion escrita es invalida")
            return "_"
        return value

    def launch(self):
        print("Hola!, escribe las instrucciones, cuando termine escribir -1")
        count_i = 0
        count_j = 0
        value = self.inputInstruction(count_i,count_j)
        while(value != "-1" and count_i <= 9 and count_i <= 9):
            self.memory.writeInMemory(value,count_i,count_j)
            if count_j <= 8 and value != "_":
                count_j += 1
            elif(value != "_"):
                count_i += 1
                count_j = 0
            self.memory.consolePrintMemory()
            value = self.inputInstruction(count_i,count_j)
    
    def defInstruction(self,data,i,j):
        self.memory.writeInMemory(data,i,j)

