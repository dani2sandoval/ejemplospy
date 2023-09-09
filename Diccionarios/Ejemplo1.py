# En el bloque principal del programa definir un diccionario que alamacene 
# Nombres de paises claves y como valor la cantidad de habitantes 

def imprimir (paises):
    for clave in paises:
        print (clave, paises[clave])

# Bloque Principal
paises = {"Argentina": 4000000, "España": 4600000, "Brasil": 19000000, "Uruguay": 3400000}
imprimir(paises)