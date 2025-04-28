# Lista de clientes
clientes = ["ana", "", "JORGE", "maria", "   ", "luis", "CARLA"]

# Recorrer la lista
for i, nombre in enumerate(clientes, start=1):
    nombre_limpio = nombre.strip()  # Eliminamos espacios extra
    if not nombre_limpio:  # Si el nombre está vacío después de limpiar
        print(f"⚠️ Alerta: Cliente {i} tiene un nombre no válido (vacío).")
    else:
        nombre_formateado = nombre_limpio.capitalize()
        print(f"Cliente {i}: {nombre_formateado}")
