#se realiza una carga de valores por teclado,
#se almacenan en una lista
#Al finalizar se muestra el tamaño de la lista

lista =[]

valor = int(input("ingrese un valor (Agregar O para finalizar)"))

while valor !=0:
    lista.append(valor)
    valor = int(input("ingrese un valor (Agregar O para finalizar)"))

print ("Tamaño de la lista de datos: ")
print (len(lista))
