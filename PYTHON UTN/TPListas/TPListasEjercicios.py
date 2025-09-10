# Ejercicio 1
lista = []

for i in range(1, 100): 
    if(i % 4 == 0): 
        lista.append(i)

print(lista)

# Ejercicio 2
listaRandom = [1,2,3,"soy el sujeto",41]
print(listaRandom[-2])

# Ejercicio 3
lista = []
lista.append("primero")
lista.append("segundo")
lista.append("tercero")

print(lista)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

# Ejercicio 5 Explicacion: Este codigo lo que hace es eliminar el elemento mas grande de la lista
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

# Ejercicio 6
lista = [i for i in range(10,31,5)]
print(lista[0:2])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "me cambiaron"
autos[2] = "a mi tambien we"

print(autos)

# Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

# Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)