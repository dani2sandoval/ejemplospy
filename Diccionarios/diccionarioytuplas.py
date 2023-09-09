# Confeccionar un Programa que permita cargar un código de producto como
# Código producto, almacenar clave y nombre de producto
# 1. Carga de datos en el diccionario
# 2. Listado completo de productos
# 3. Consulta de un producto por su clave, mostrar precio y stock
# 4. Listado de todos los productos que tengan stock 0

def cargar():
    productos={}
    continuar = "s"
    while continuar == "s":
        codigo = int (input("Ingrese el código del producto: "))
        descripcion = int (input("Ingrese una descripción del producto: "))
        precio= int (input("Ingrese el precio del producto: "))
        stock = int (input("Ingrese el stock actual: "))
        productos[codigo]= (descripcion, precio, stock)
        continuar = input("Desea cargar otro producto: [s/n]")
    return productos

def imprimir (productos):
    print ("Listado de Productos: ")
    for codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

def consulta (productos):
    codigo= int (input("Ingrese el código de articulo a cosultar: "))
    if codigo in productos:
        print(productos[codigo][0], productos[codigo][1], productos[codigo][2])

def listado_stock_cero(productos):
    print("Listado de Productos con stock 0: ")
    for codigo in productos:
        if productos [codigo][2] == 0:
            print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

# Bloque principal

productos = cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)