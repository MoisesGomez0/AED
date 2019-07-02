from ListaEjemplo2LibroClases import *
lista = LinkedList()
lista.add(4)
lista.add(1)
lista.add(1)
lista.add(1)
lista.add(1)
lista.add(1)
lista.add(4)

lista.showInColose()
lista.purgeSelf()
print()

newLista = lista.purge()
newLista.showInColose()
