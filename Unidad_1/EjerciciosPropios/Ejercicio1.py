#Este algoritmo convierte una catidad en n cantidades de billetes equvalentes
value = int(input("Escriba el monto: "))
billetes = []

while value > 0:
    if value >= 500:
        billetes.append(500)
        value -= 500
    elif value >= 100:
        billetes.append(100)
        value -= 100
    elif value >= 50:
        billetes.append(50)
        value -= 50
    elif value >= 20:
        billetes.append(20)
        value -= 20
    elif value >= 10:
        billetes.append(10)
        value -= 10
    elif value >= 5:
        billetes.append(5)
        value -= 5
    elif value >= 2:
        billetes.append(2)
        value -= 2
    elif value >= 1:
        billetes.append(1)
        value -= 1
print(billetes)
if billetes.count(500) > 0:
    print(billetes.count(500), "Billetes de 500")
if billetes.count(100) > 0:
    print(billetes.count(100), "Billetes de 100")
if billetes.count(50) > 0:
    print(billetes.count(50), "Billetes de 50")
if billetes.count(20) > 0:
    print(billetes.count(20), "Billetes de 20")
if billetes.count(10) > 0:
    print(billetes.count(10), "Billetes de 10")
if billetes.count(5) > 0:
    print(billetes.count(5), "Billetes de 5")
if billetes.count(2) > 0:
    print(billetes.count(2), "Billetes de 2")
if billetes.count(1) > 0:
    print(billetes.count(1), "Billetes de 1")
