import random
"""
Map: Map(function,iterable), Map devuelve un objeto de tipo Map que se puede castear a
    lista mediante list(map(function,iterable)) los elementos de esta lista seran el retorno de
    function para cada elemento del iterable

Lambda: lambda x:x+1 es una función anónima de una línea esta función resive una n cantidad de
        parámetros y el retorno es lo que está despues de los dos puntos

Lista por compresion:Es una forma de crear iterables con cliclos en una linea


Ejemplo1: si tiene el arreglo [1,2,3,4], haga código de una linea que obtenga el arreglo [2,3,4,5]
"""
#forma 1

def Ejemplo1Function(x):
    return x+1

a = [1,2,3,4]
b = list(map(Ejemplo1Function,a))
print(b) # [2,3,4,5]

# foma 2 con lambda

a = [1,2,3,4]
b=list(map(lambda x:x+1,a))
print(b) #[2,3,4,5]

"""
Ejemplo2: genera la matriz [[1,2],[2,3]] en una linea y haga código de una linea que
obtenga el resultado [[3],[5]]
"""
#crear la lista por compresión

a = [[i+j for j in range(1,3)] for i in range(0,2)]
# para cada i en [0,2[ creara un arreglo que dentro tendrá el elemtento i+jpara cada j en [1,3[
print(a) # [[1,2],[2,3]]

#forma sin lambda

def Ejemplo2Function(x):
    return [x[0]+x[1]]
b = list(map(Ejemplo2Function,a))
print(b) # [[3],[5]]

#forma con lambda

b = list(map(lambda x:[x[0]+x[1]],a))
print(b) # [[3],[5]]

"""
Ejercicio 3: crear una matriz cero de orden 4 con código de una linea en python,
             junto con crear una matriz de números aleatorios de orden 4 y con map sumar ambas matrices
"""

matriz0 = [[0 for j in range(0,4)] for i in range(0,4)]
matriz1 = [[random.randint(0,100) for j in range(0,4)] for i in range(0,4)]
print(matriz1)
suma = list(
        map(
            lambda x,y: list(
                map(
                    lambda a,b:a+b,
                    x,
                    y
                )
            ),
            matriz0,
            matriz1
        )
)
print(suma)