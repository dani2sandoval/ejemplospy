# Desarrollar una función que solicite la carga del dia mes y año
# Almacenar los datos en una tupla
# Funcion para mostrar por pantalla la Tupla

def cargar_fecha ():
    dd = int(input("Ingrese el número de día: "))
    mm = int (input("Ingrese número de mes: "))
    aa = int (input("Ingrese número de año: "))
    return(dd,mm,aa)

def imprimir_fecha (fecha):
    print (fecha[0], fecha[1], fecha[2], sep="/")

# Bloque principal
fecha = cargar_fecha()
imprimir_fecha(fecha)