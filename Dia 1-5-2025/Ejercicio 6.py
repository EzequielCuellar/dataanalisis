numeros = [10, 20, -30, 40, -50]

suma = 0

for numero in numeros:

    if numero < 0:

        continue

    suma += numero

print(suma)