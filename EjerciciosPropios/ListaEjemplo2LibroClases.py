class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.first = None
#Imprime el valor de todos los nodos
    def showInColose(self):
        current = self.first
        while(current.next):
            print(current.value)
            current = current.next
        print(current.value)
#Añade un nodo al final de la lista
    def add(self, value):
        if (not self.first):
            self.first = Node(value)
        else:
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
#Retorna el primer nodo con valor igual al parametro value
    def find(self,value):
        current = self.first
        while current:
            if current.value == value:
                return current
            current = current.next
        return False
#Elimina todos los nodos que tengan como valor el parámetro value
    def deleteAll(self,value):
        current = self.first
        previous = self.first
        condition = False
        if current.value == value:
            self.first = current.next
        else:
            current = current.next
            while current:
                if current.value == value:
                    previous.next = previous.next.next
                    current = previous.next
                else:
                    current = current.next
                    previous = previous.next
#Elimina el primer nodo que tenga como valor el parámetro value
    def deleteFirst(self,value):
        current = self.first
        previous = self.first
        condition = False
        if current.value == value:
            self.first = current.next
        else:
            current = current.next
            while current:
                if current.value == value:
                    previous.next = previous.next.next
                    current = previous.next
                    return True
                else:
                    current = current.next
                    previous = previous.next
#Elimina todos los nodos repetidos dejando solo el primer nodo que tenga tal valor
    def purgeSelf(self):
        test = self.first
        current = test.next
        previous = test
        while test:
            while current:
                if test.value == current.value:
                    previous.next = previous.next.next
                    current = previous.next
                else:
                    previous = previous.next
                    current = current.next
            test = test.next
            if test:
                current = test.next
                previous = test

    def purge(self):
        newList = LinkedList()
        newList.first = self.first
        test = newList.first
        current = test.next
        previous = test
        while test:

            while current:
                if test.value == current.value:
                    previous.next = previous.next.next
                    current = previous.next
                else:
                    previous = previous.next
                    current = current.next
            test = test.next
            if test:
                current = test.next
                previous = test
            else:
                return newList
#Ese método retorna el primer nodo
    def getFirst(self):
        return self.first
#Retornar el último nodo
    def getLast(self):
        temp = self.first
        while(temp.next):
            temp = temp.next
        return temp
#Añade un nodo en la posición que tenga como número el valor n
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
