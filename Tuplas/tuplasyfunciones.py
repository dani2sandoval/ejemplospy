# Almacenar en una lista de 5 elementos las tuplas con el nombre de los empleados.
# Implementar las siguientes funciones:
# Craga de Empleados
# impresión de los empleados y sueldo
# Nombre del empleado con el mayor sueldo
# Cantidad de empledos con el sueldo menor a 1000


def  cargar ():
    empelados = []
    for x in range (5):
        nombre = input("Nombre del empleado: ")
        sueldo = input ("Ingrese el sueldo del empleado: ")
        empelados.append(nombre, sueldo)
    return empelados

def impimir(empleados):
    print("Listado de los empleados y sus sueldos: ")
    for nombre, sueldo in empleados: 
        print (nombre, sueldo)

def mayor_sueldo(empleados):
    empleado=empleados[0]
    for emp in empleado:
        if emp[1]>empleados[1]:
            empleado= emp
    print("Empleado con el mayor sueldo:", empleado[0], "su sueldo es:", empleado[1])

def menor_sueldo(empleados):
    cant= 0 
    for empleado in empleados:
        if empleado[1]<1000:
            cant = cant+1
    print("Cantidad de Empelados con el sueldo menor a 1000: ", cant)

#Bloque Principal

empleados= cargar()
imprimir = impimir(empleados)
mayor_sueldo1 = mayor_sueldo(empleados)
salario_menor = menor_sueldo(empleados)