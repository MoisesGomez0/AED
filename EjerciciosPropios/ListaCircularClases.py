#-*- coding: utf-8 -*-
import os

#Definición de nodo
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class CircularLinkledList():
    def __init__(self):
        self.first = None
        self.last = None

    def add(self,value):
        if not self.first:
            self.first = Node(value)
            self.first.next = self.last
            return True
        elif not self.last:
            self.last = Node(value)
            self.last.next = self.first
            self.first.next = self.last
            return True
        else:
            current = self.first
            temp = self.first.next
            while current != self.last:
                current = current.next
                print(current.value)
            self.last = Node(value)
            current.next = self.last
            self.last.next = self.first
            self.first.next = temp
            return True


    def showInColose(self):
        current = self.first
        while current != self.last and current:
            print(current.value)
            current = current.next
        print(current.value)