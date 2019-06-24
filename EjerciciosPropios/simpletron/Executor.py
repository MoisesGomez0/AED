from Memory import *

class Executor():
    def __init__(self,memory):
        self.memory = memory
    def executor(self):
        array = self.memory.getMemory()
        for i in array:
            for j in i:
                if len(j) == 4 :
                    if j[:2] == "01":
                        