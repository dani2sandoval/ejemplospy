def cargar():
    agenda = {}
    continuar = "s"
    while continuar == "s":
        fecha = input("Ingrese la fecha en formato dd/mm/aa: ")
        continuar2 = "s"
        lista = []
        while continuar2 == "s":
            hora = input("Ingrese la hora de la actividad con formato hh:mm: ")
            actividad = input("Ingrese la descripción de su actividad: ")
            lista.append((hora, actividad))  
            continuar2 = input("Ingrese otra actividad para la misma fecha: [s/n]")
        agenda[fecha] = lista  
        continuar = input("Ingresa otra fecha: [s/n]")
    return agenda

def imprimir(agenda):
    print("Listado completo de la agenda: ")
    for fecha in agenda:
        print("Para la fecha: ", fecha)
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)

def consulta_fecha(agenda):
    fecha = input("Ingrese la fecha que desea consultar: ")
    if fecha in agenda:
        print(f"Actividades para la fecha {fecha}:")
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)
    else:
        print("No hay actividades para esta fecha.")

# Bloque Principal
agenda = cargar()
imprimir(agenda)
consulta_fecha(agenda)