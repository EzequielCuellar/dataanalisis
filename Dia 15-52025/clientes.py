# Lista para guardar los nombres de los y las clientes
nombres_clientes = []

print("Ingresá los nombres de los y las clientes. Escribí 'fin' para terminar.")

while True:
    nombre = input("Nombre: ").strip()
    
    if nombre.lower() == "fin":
        break
    elif nombre == "":
        print("⚠️ El nombre no puede estar vacío. Por favor, intentá de nuevo.")
    else:
        nombres_clientes.append(nombre)

# Ordenar alfabéticamente la lista de nombres
nombres_clientes.sort()

# Mostrar la lista ordenada
print("\nLista de clientes ordenada alfabéticamente:")
for nombre in nombres_clientes:
    print("-", nombre)
