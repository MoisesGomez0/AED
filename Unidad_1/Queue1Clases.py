class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
    def push(self,value):
        if(not self.first):
            self.first = Node(value)
        else:
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
    def pop(self):
        temp = self.first
        self.first = self.first.next
        return temp
    def getFirstValue(self):
        return self.first.value
    def getLastValue(self):
        temporalNode = self.first
        while(temporalNode.next):
            temporalNode = temporalNode.next
        return temporalNode.value
    def showAllValues(self):
        current = self.first
        while(current.next):
            print(current.value)
            current = current.next
        print(current.value)