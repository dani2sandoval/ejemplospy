# Agregar 5 nombres de personas en un arreglo con sus respectivas edades 
# Realizar las carga por teclado; 
# Todos los datos imprimir los nombres de las personas mayores de edad 18 Años (Mayores o Iguales a 18 años)

nombres =[]
edades = []

for x in range(5):
    nom = input("Ingrese el nombre de la persona ")
    nombres.append(nom)
    ed = int (input("Ingrese la edad de dicha persona: "))
    edades.append(ed)

print ("Nombre de las personas mayores de edad: ")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])