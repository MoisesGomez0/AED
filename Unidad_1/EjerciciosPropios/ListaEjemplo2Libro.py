from ListaEjemplo2LibroClases import *
lista1 = LinkedList()
lista1.add(4)
lista1.add(1)
lista1.add(1)
lista1.add(1)
lista1.add(1)
lista1.add(1)
lista1.add(4)

print("Esta es la lista 1")
lista1.showInColose()
print("\n")

lista2 = LinkedList()
lista2.add("a")
lista2.add("b")
lista2.add("c")
lista2.add("d")
lista2.add("e")
lista2.add("f")
lista2.add("g")
lista2.add("h")

print("Esta es la lista 2")
lista2.showInColose()
print("\n")

lista3 = JoinLists(lista1,lista2)
print("Esta es la lista 3 union de la lista 1 con la 2")
lista3.showInColose()

lista3.addAfter("Prueba",1)
print("Lista 3 luego de agregar 'prueba' depues de 1")
lista3.showInColose()
buscando = 1
print("En la lista 3 en cuentra %s, %s veces" %(buscando,lista3.count(buscando)))