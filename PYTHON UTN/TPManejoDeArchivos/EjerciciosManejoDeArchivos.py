productos_iniciales = [
    "Manzana,50,100\n",
    "Leche,80,50\n",
    "Pan,40,200\n"
]

# 1
with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    archivo.writelines(productos_iniciales)
    print("Archivo creado")

# 2
with open("productos.txt", "r", encoding="utf-8") as archivo: 
    lineas = archivo.readlines()    
    
    for linea in lineas[1:]:  # ignorar encabezado
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    
# 3
print("\nAgregar nuevo producto:")
nombre = input("Nombre: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("\nProducto agregado correctamente")

# 4
productos = []  
with open("productos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for linea in lineas[1:]:  # ignorar encabezado
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print("\nLista de productos:")
for p in productos: 
    print(p) 

# 5
buscar = input("\nIngrese el nombre del producto a buscar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print("\nProducto encontrado:")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nNo se encontró ningún producto con ese nombre")

# 6
with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado correctamente con todos los productos.")
