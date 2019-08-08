class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def add(self,value):
        if(not self.first):
            self.first = Node(value)
        else:
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
    
    def _print(self):
        temp=self.first
        while(temp.next):
            print(temp.value)
            temp = temp.next
        print(temp.value)
    
    def getFirst(self):
        return self.first
    
    def getLast(self):
        temp = self.first
        while(temp.next):
            temp = temp.next
        return temp
    def addInPosition(self,value,n):
        if(n == 0):
            temp = self.first
            self.first = Node(value)
            self.firt.next = temp
            return True
        elif(n>1):
            count = 0
            temp = self.first
            tempPre = self.first
            while(temp.next):
                temp = temp.next
                count+=1
                if(count == n):
                    tempPre.next = Node(value)
                    (tempPre.next).next = temp
                    return True
                tempPre = tempPre.next
        return False
