#Observá este programa. ¿Qué mostrará si se ingresa "Lunes"?#

dia = input("Ingresá un día de la semana: ")

match dia:

    case "Lunes":

        print("Inicio de semana.")

    case "Viernes":

        print("Fin de semana.")

    case _:

        print("Día intermedio.")
