class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList():
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
            current.next.prev = current
    def show(self):
        now = self.first
        while now.next:
            print(now.value)
            now = now.next
        print(now.value)
    
    def showReverse(self):
        now = self.first
        while now.next:
            now = now.next

        while now.prev:
            print(now.value)
            now = now.prev
        print(now.value)
