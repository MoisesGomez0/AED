class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.first = None
    
    def add(self,value):
        if not self.first:
            self.first = Node(value)
            self.first.next = self.first
        else:
            current = self.first
            while current.next != self.first:
                current = current.next
            current.next = Node(value)
            current.next.next = self.first
    
    def show(self):
        temporal = self.first
        while temporal.next != self.first:
            print(temporal.value)
            temporal = temporal.next
        print(temporal.value)