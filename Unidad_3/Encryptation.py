# -*- coding:utf8 -*-
class Encryptor:
    def __init__(self):
        pass

    def decrypt(self,encryptedPhrase,password):
        return self.encrypt(encryptedPhrase,password)

    def encrypt(self,phrase,password):
        return "".join(list(map(lambda x:chr(x^ord(password[0])),bytearray(phrase,"ascii"))))
    
    def encryptV2(self,phrase,password):
        password = bytearray(password,"utf8")
        c = 0
        encrypt = []
        for i in bytearray(phrase,"utf8"):
            encrypt.append(chr(i^password[c%len(password)]))
            c += 1
        return "".join(encrypt)

    def decryptV2(self,phrase,password):
        return self.encryptV2(phrase,password)

e = Encryptor()



encryptedPhrase = e.encrypt("Hola Mundo","contraseña")
print(encryptedPhrase)
print(e.decrypt(encryptedPhrase,"contraseña"))
print("-"*20)
encryptedPhrase = e.encryptV2("Hola Mundo","contraseña")
print(encryptedPhrase)
print(e.decryptV2(encryptedPhrase,"contraseña"))