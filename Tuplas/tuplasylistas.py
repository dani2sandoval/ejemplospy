# definir una Tupla de 3 valores
# Convertir el contenido de las tuplas a tipo lista, Modificar la lista y luego que sea una tupla nuevamente

fecha_tupla1=(25,12,2016)
print("Impresión de la primera tupla:")
print (fecha_tupla1)

#Copiamos la lista a una tupla
fecha_lista = list(fecha_tupla1)
print ("Imprimimos la lista copiada: ")
print (fecha_lista)

#Modificamos la lista
fecha_lista[0]= 31
print ("Imprimimos la lista ya modificada: ")
print (fecha_lista)

# Copiamos la lista Modificada a una Tupla
fecha_tupla2 = tuple(fecha_lista)
print ("Tupla modificada: ")
print (fecha_tupla2)