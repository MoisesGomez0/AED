#-*- coding:utf-8 -*-
"""
Tupla: Una lista inmutable de elementos,
    Declaración: A = (a,b,c)
    para acceder a elementos: x,y,z = A, donde será x=a, y=b, z=c
    Métodos:
        count()
        Sea la tupla A, b = A.count(value)
        b es igual al número de veces que aparece value en la tuple

        index()
        Sea la tupla A, b = A.index(value)
    b es igual a el número de índice del primer valor value



    Ejemplo de for con una tupla por iterador:
        for a,b in [[1,2],[3,4],[5,6]]:
            print("a:",a,"b:",b)
        Salida:
            a:1 b:2
            a:3 b:4
            a:5 b:6

Diccionario: Es una estructura de datos parecida a una lista, donde en lugar
de índice numérico ([0,1,2,3]) es una cadena o "key" (["city","time","date"])
    Declaración: A = {"name":"carlos","childrens":[{"name":"juan"},{"name":"maria"}]}
    Métodos:
        dict ()
        Recibe como parámetro una representación de un diccionario y si es factible, 
        devuelve un diccionario de datos.
        dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)
        dic → {‘nombre’ : 'nestor', ‘apellido’ : 'Plasencia', ‘edad’ : 22}

        zip()
        Recibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla.
        Ambos parámetros deben tener el mismo número de elementos.
        Se devolverá un diccionario relacionando el elemento i-esimo de cada uno de los iterables.
        dic = dict(zip('abcd',[1,2,3,4]))
        dic →   {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}

        items()
        Devuelve una lista de tuplas, cada tupla se compone de dos elementos: 
        el primero será la clave y el segundo, su valor.
        dic =   {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        items = dic.items()
        items → [(‘a’,1),(‘b’,2),(‘c’,3),(‘d’,4)]

        keys()
        Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
        dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        keys= dic.keys()
        keys→ [‘a’,’b’,’c’,’d’] 

        values()
        Retorna una lista de elementos, que serán los valores de nuestro diccionario.
        dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        values= dic.values()
        values→ [1,2,3,4] 

        clear()
        Elimina todos los ítems del diccionario dejándolo vacío.
        dic 1 =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        dic1.clear()
        dic1 → { }

        copy()
        Retorna una copia del diccionario original.
        dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        dic1 = dic.copy()
        dic1 → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}

        fromkeys()
        Recibe como parámetros un iterable y un valor, devolviendo un diccionario que 
        contiene como claves los elementos del iterable con el mismo valor ingresado. 
        Si el valor no es ingresado, devolverá none para todas las claves.

        dic = dict.fromkeys(['a','b','c','d'],1)
        dic →  {‘a’ : 1, ’b’ : 1, ‘c’ : 1 , ‘d’ : 1}

        get()
        Recibe como parámetro una clave, devuelve el valor de la clave. 
        Si no lo encuentra, devuelve un objeto none.
        dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        valor = dic.get(‘b’) 
        valor → 2

        pop()
        Recibe como parámetro una clave, elimina esta y devuelve su valor. 
        Si no lo encuentra, devuelve error.
        dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        valor = dic.pop(‘b’) 
        valor → 2
        dic → {‘a’ : 1, ‘c’ : 3 , ‘d’ : 4}

        setdefault()
        Funciona de dos formas. En la primera como get
        dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        valor = dic.setdefault(‘a’)
        valor → 1
        Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.
        dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        valor = dic.setdefault(‘e’,5)
        dic → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4 , ‘e’ : 5}

        update()

        Recibe como parámetro otro diccionario. Si se tienen claves iguales, 
        actualiza el valor de la clave repetida; si no hay claves iguales, 
        este par clave-valor es agregado al diccionario.
        dic 1 = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        dic 2 = {‘c’ : 6, ’b’ : 5, ‘e’ : 9 , ‘f’ : 10}
        dic1.update(dic 2)
        dic 1 → {‘a’ : 1, ’b’ : 5, ‘c’ : 6 , ‘d’ : 4 , ‘e’ : 9 , ‘f’ : 10}

    Ejemplos:
    A = {"name":"carlos","childrens":[{"name":"juan"},{"name":"maria"}]}
        (1) print(A["name"])
        salida:
            carlos

        (2) print(A["childrens"])
        salida:
            [{'name': 'juan'}, {'name': 'maria'}]

        (3) print(A["childrens"][0])
        salida:
            {'name': 'juan'}
        
    A={"x":1,"y":2,"z":3}

        (4) print(A)
        salida:
            {"x":1,"y":2,"z":3}

        (5)
        for i in A:
            print(i)
        salida:
        x
        y
        z

        (6)
        for i in A:
            print(A[i])
        salida:
        1
        2
        3

        (7)
        for k,v in A.items():
            print("key:",k,"value:",v)
        salida:
            key: x value: 1
            key: y value: 2
            key: z value: 3

JSON:(JavaScript Object Notation-Notación de Objetos de JavaScript) 
es un formato ligero de intercambio de datos, stá constituído por dos estructuras:
    Una colección de pares de nombre/valor. En varios lenguajes esto es conocido como un objeto, registro, estructura, diccionario, tabla hash, lista de claves o un arreglo asociativo.
    Una lista ordenada de valores. En la mayoría de los lenguajes, esto se implementa como arreglos, vectores, listas o sequencias.


"""

""" A = {"name":"Carlos","age":8,
"childrens":{
    {"name":"Juan","age":15,"childrens":{}},
    {"name":"Maria","age":50,"childrens":{
        {"name":"Estiven","age":5,"childrens":{}},
        {"name":"Moises","age":57,"childrens":{}}
    }}
    }
    }
for i in A:
    print """

class Tree:
    def __init__(self,json):
        self.json = json
    def show(self):
        self.showInner(self.json)
    def showInner(self,json,tab=""):
        for i in json:
            if type(json[i]) == dict:
                print("%s%s:"%(tab,i))
                self.showInner(json[i],"%s%s"%(tab,"\t"))
            else:
                print("%s%s:%s"%(tab,i,json[i]))

A = {"carlos":
    {"name":"Carlos Mejia","age":1,"childrens":{
        "maria":{"name":"Maria Ramos","age":25,"childrens":{}},
        "juan":{"name":"Juan Hernandez","age":50,"childrens":{
            "josé":{"name":"José Rivera","age":52,"childrens":{}}
    }}
}}}

tree = Tree(A)
tree.show()