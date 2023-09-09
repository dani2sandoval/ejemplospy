#Crear y cargar una lista con 5 enteros por teclado
#Implementación de algoritmo

lista = []

for x in range (5):
    valor= int(input("Ingrese un Número: "))
    lista.append(valor)

menor = lista[0]
posicion = 0

for x in range (1,5):
    if lista[x]< menor:
        menor= lista[x]
        posicion = x

print("Lista Completa en una Matriz: ")
print (lista)
print ("menor de la lista: ")
print (menor)
print ("Posición en la lista: ")
print (posicion)