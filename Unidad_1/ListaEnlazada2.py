from ListaEnlazada2Clases import *
Lista = LinkedList()
Lista.add(1)
Lista.add(2)
Lista.add(3)
Lista.add(4)
Lista.add(5)
Lista.add(6)

print("La lista en orden es: ")
Lista._print()

print("El primero de la lista es ",Lista.getFirst().value)
print("El último de la lista es ",Lista.getLast().value)

Lista.addInPosition("Kevin se la come",5)
print("La lista en orden es: ")
Lista._print()