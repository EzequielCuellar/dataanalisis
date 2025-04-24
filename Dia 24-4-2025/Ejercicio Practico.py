apellido = input("Apellido por favor: ")
nombre = input("Nombre por favor: ")
correo = input("Correo por favor: ")

while True:
    edad_input = input("Edad por favor: ")
    try:
        edad = int(edad_input)
        if edad < 0:
            print("Por favor, ingrese una edad válida (número positivo).")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")

if edad < 18:
    rango_etario = "Menor de edad"
elif 18 <= edad < 60:
    rango_etario = "Adulto"
else:
    rango_etario = "Adulto mayor"

ingresos = []
mes = 1

while mes <= 6:
    try:
        ingreso = float(input(f"Ingresá el ingreso del mes {mes}: "))
        if ingreso < 0:
            print("El valor ingresado no es válido. Debe ser un número positivo.")
            continue
        ingresos.append(ingreso)
        mes += 1
    except ValueError:
        print("Por favor, ingresá un número válido.")

total_final = sum(ingresos)

print("\n--- Datos ---")
print(f"Nombre y apellido: {apellido}, {nombre}")
print(f"Correo electrónico: {correo}")
print(f"Rango etario: {rango_etario}")
print(f"Total final: ${total_final:.2f}")
