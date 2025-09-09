# Ejercicio 1
for i in range(101): 
    print(i) 

# Ejercicio 2
num: int = int(input("Ingrese un numero: "))
cont = 0

while num > 0:
    num = num // 10   
    cont += 1

print(f"Los dígitos del numero son: {cont}")

# Ejercicio 3
num1: int = int(input("Ingrese el primer numero: "))
num2: int = int(input("Ingrese el segundo numero: "))
suma: int = 0
while num1 <= num2:     
    suma += num1 
    num1 += 1 

print(f"La suma de los numeros ingresados es: {suma}")

# Ejercicio 4
suma = 0
while True: 
    num: int = int(input("Ingrese un numero: "))

    if(num == 0):
        break

    suma += num
    print(f"Suma: {suma - num} + {num} = {suma}")

print("Terminamos")

# Ejercicio 5
import random
numAleatorio: int = random.randint(0, 9)

while True: 
    num: int = int(input("Adivina el numero: "))

    if(num == numAleatorio):
        print(f"¡Adivinaste! El numero es: {numAleatorio}")
        break
    
    else: 
        print("Fallaste, sigue intentando...")

# Ejercicio 6
for i in range(0, 102, 2): 
    print(i)

# Ejercicio 7
num :int = int(input("Ingrese un numero: "))
suma :int = 0
i :int = 0

while i <= num:
    suma += i
    i += 1

print(f"La suma hasta tu numero es: {suma}")

# Ejercicio 8
pares :int = 0
impares :int = 0
negativo: int = 0
positivo: int = 0

for i in range(100): 
    num :int = int(input("Ingrese un numero: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1

print(f"Cantidad de pares: {pares}\nCantidad de impares: {impares}\nCantidad de negativos: {negativo}\nCantidad de positivos: {positivo}") 

# Ejercicio 9
suma :int = 0

for i in range(100): 
    num :int = int(input("Ingrese un numero: "))
    suma += num

media: float = suma / 100 
print(f"Promedio: {media}") 


# Ejercicio 10
num = int(input("Ingrese un número: "))
invertido = 0

while num > 0:
    digito = num % 10         
    invertido = invertido * 10 + digito
    num = num // 10            

print("Número invertido:", invertido)

