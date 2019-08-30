class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
    
    def add(self,value):
        if not self.first:
            self.first = Node(value)
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = Node(value)
    
    def count(self):
        counter = 0
        current = self.first
        while current:
            counter+=1
            current = current.next
        return counter
    
    def getValueIndex(self,index):
        if not self.first or index>self.count()-1:
            return "None"
        elif index == 0:
            return self.first.value
        else:
            current = self.first.next
            for i in range(1,index):
                current = current.next
            return current.value
