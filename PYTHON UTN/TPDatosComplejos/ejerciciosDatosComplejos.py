# Ejercicio 1
precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva':
1450}

precios_frutas.update({"naranja": 1200, "manzana": 1500, "pera": 2300})

print(precios_frutas)

# Ejercicio 2
precios_frutas.update({"banana": 1330, "manzana": 1700, "melon": 2800})

print(precios_frutas)

# Ejercicio 3
frutas_lista = []

for fruta in precios_frutas.keys(): 
    frutas_lista.append(fruta)

print(frutas_lista)

# Ejercicio 4
contactos = {}
for i in range(3): 
    while True:
        nombre_contacto = input("Ingrese nombre de contacto: ").strip()
        if nombre_contacto == "":
            print("El nombre no puede estar vacio")
        elif nombre_contacto in contactos:
            print("Ese contacto ya existe")
        else:
            break

    while True:
        num_contacto = input(f"Ingrese número de contacto de {nombre_contacto}: ").strip()
        if num_contacto == "":
            print("El numero no puede estar vacio")
        elif not num_contacto.isdigit():
            print("El numero debe contener solo digitos")
        else:
            break

    contactos[nombre_contacto] = num_contacto

pedir_contacto = input("Buscar usuario: ")

if(pedir_contacto in contactos): 
    print(f"Numero del contacto {pedir_contacto}: ", contactos.get(pedir_contacto))
else: 
    print("El contacto no existe")

# Ejercicio 5
frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(recuento)

# Ejercicio 6
alumnos = {}

for i in range(3): 
    notas_lista = []
    while True:
        nombre_alumno = input("Ingrese nombre de contacto: ").strip()
        if nombre_alumno == "":
            print("El nombre no puede estar vacio")
        else:
            break

    for j in range(3):
        while True:
            nota_alumno = input(f"Ingrese nota {j+1} de {nombre_alumno}: ").strip()
            if nota_alumno == "":
                print("La nota no puede estar vacia")
            elif not nota_alumno.isdigit():
                print("La nota debe ser un numero entero")
            else:
                notas_lista.append(int(nota_alumno))
                break
    
    alumnos[nombre_alumno] = tuple(notas_lista)

print(f"NOTAS ALUMNOS: {alumnos}")

# Ejercicio 7
parcial1 = {"Ana", "Juan", "Pedro", "Lucía"}
parcial2 = {"Juan", "Lucía", "María", "Carlos"}

# Ambos
ambos = parcial1.intersection(parcial2)
print("Aprobaron ambos parciales:", ambos)

# Solo uno 
solo_uno = parcial1.symmetric_difference(parcial2)
print("Aprobaron solo uno de los dos parciales:", solo_uno)

# Al menos uno
total = parcial1.union(parcial2)
print("Aprobaron al menos un parcial:", total)

# Ejercicio 8
stock = {
    "Manzana": 50,
    "Leche 1L": 20,
    "Pan integral": 15,
    "Huevos (docena)": 12,
    "Arroz 1kg": 30,
    "Aceite 1L": 10,
    "Queso porción": 8,
    "Tomate": 40
} 

def consultarStock(producto): 
    if(producto in stock): 
        print(f"{producto} stock: {stock.get(producto)}")
    else: 
        print("El producto no esta en stock")        

def añadirUnidades(producto): 
    stock[producto] = stock.get(producto, 0) + 1
    print(f"Se añadio una unidad mas al producto '{producto}'")

def añadirProducto(producto): 
    if(producto not in stock): 
        stock[producto] = 1
        print(f"Se añadio el producto '{producto}'")
    else: 
        print("El producto ya existe")    
    
while True:
    print("\n=== MENÚ DE STOCK ===")
    print("0. Salir")
    print("1. Consultar stock de un producto")
    print("2. Agregar una unidad a un producto existente")
    print("3. Agregar un nuevo producto")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        consultarStock(producto.capitalize())

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        añadirUnidades(producto.capitalize())

    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        añadirProducto(producto.capitalize())

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

# Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:30"): "Ir al gimnasio",
    ("Miércoles", "09:00"): "Clase de inglés",
    ("Viernes", "18:00"): "Cena con amigos"
}

def consultarEvento(dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        print(f"El {dia} a las {hora} tenes: {agenda[clave]}")
    else:
        print(f"No hay ninguna actividad programada el {dia} a las {hora}")

print("CONSULTA DE AGENDA")
dia = input("Ingrese el dia: ").capitalize()
hora = input("Ingrese la hora (ej. 14:00): ")

consultarEvento(dia, hora)

paises = {
    "argentina": "Buenos Aires",
    "chile": "Santiago",
    "uruguay": "Montevideo",
    "brasil": "Brasilia",
    "peru": "Lima",
    "paraguay": "Asunción",
    "bolivia": "La Paz",
    "colombia": "Bogotá",
    "mexico": "Ciudad de México"
}

# Ejercicio 10
paises_lista = []
capitales = []
paises_invertido = {}

for pais in paises.keys():
    paises_lista.append(pais)
for capital in paises.values(): 
    capitales.append(capital)

for i in range(len(paises)): 
    paises_invertido[capitales[i]] = paises_lista[i] 

print(paises_invertido)