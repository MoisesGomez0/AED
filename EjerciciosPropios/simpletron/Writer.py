class Writer():
    def __init__(self,memory):
        self.memory = memory
    def memoryWriter(self,data,i,j):
            self.memory[i][j] = data
