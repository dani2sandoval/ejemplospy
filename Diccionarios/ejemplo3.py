# Desarrollar una app que nos permita crear un diccionario
# Ingles Castellano. La clave es la palabra en ingles y el valor es la palabra en castellano
# Crear
# Cargar el diccionario
# Listado completo del diccionario
# Ingresar por teclado una palabra en inglés y si existe en el diccionario

def cargar():
    diccionario = {}
    continuar= "s"
    while continuar == "s":
        caste=input("Ingrese palabra en Castellano: ")
        ing = input("Ingrese palabra en Inglés: ")
        diccionario[ing]= caste
        continuar = ("Quiere cargar otra palabra: [s/n]")
    return diccionario

def imprimir (diccionario):
    print("Listado Completo del diccionario: ")
    for ingles in diccionario:
        print (ingles, diccionario[ingles])

def consulta_palabra(diccionario):
    pal = input("Ingrese la palabra en Inglés a Consultar: ")
    if pal in diccionario:
        print("En castellano significa: ", diccionario[pal])


# Bloque Principal
diccionario = cargar()
imprimir(diccionario)
consulta_palabra(diccionario)