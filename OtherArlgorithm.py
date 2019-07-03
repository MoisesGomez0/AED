#-*- coding: utf-8 -*-
class OtherAlgorithm:
    def __init__(self):
        pass
    def factorial(self,n):
        result = 1
        for i in range(1,n+1):
            print("i=%s" %i)
            result *= i
        return result
    def factorialDesc(self,n):
        result = 1
        for i in range(n,0,-1):
            print("i=%s" %i)
            result *= i
        return result

oa = OtherAlgorithm()
n = 5
print("El factorial de %s es %s" %(n,oa.factorial(n)))
print("El factorial de %s es %s" %(n,oa.factorialDesc(n)))