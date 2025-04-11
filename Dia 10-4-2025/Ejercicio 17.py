def formatear_nombre(texto):
    return ' '.join([palabra.capitalize() for palabra in texto.strip().split()])

def validar_email(correo):
    correo = correo.replace(" ", "")
    if correo.count("@") == 1:
        return correo
    else:
        return None  

def clasificar_edad(edad):
    if edad < 15:
        return "Niño/a"
    elif 15 <= edad <= 18:
        return "Adolescente"
    else:
        return "Adulto/a"


def procesar_usuario(nombre, apellido, correo, edad):
    nombre_fmt = formatear_nombre(nombre)
    apellido_fmt = formatear_nombre(apellido)
    correo_validado = validar_email(correo)
    rango = clasificar_edad(edad)

    if correo_validado is None:
        return "Correo electrónico inválido."

    return {
        "nombre": nombre_fmt,
        "apellido": apellido_fmt,
        "correo": correo_validado,
        "rango_etario": rango
    }


usuario = procesar_usuario("maria   jose", "péREz lÓPEZ", "maria @correo.com", 17)
print(usuario)
