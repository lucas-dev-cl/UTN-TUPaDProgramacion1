#Ejercicio 1
print("Ejercicio 1")
edad: int = int(input("Ingrese su edad: "))

if(edad > 18): 
    print("Es mayor de edad.")

#Ejercicio 2
print("Ejercicio 2")
nota: int = int(input("Ingrese su nota: "))

if(nota >= 6): 
    print("Aprobado.")
else: 
    print("Desaprobado.")

#Ejercicio 3
print("Ejercicio 3")
num: int = int(input("Ingrese un numero: "))

if(num % 2 == 0): 
    print("Ha ingresado un numero par.")
else: 
    print("Por favor, ingrese un numero par.")

#Ejercicio 4
print("Ejercicio 4")
edad: int = int(input("Ingrese su edad: "))

if(edad < 12): 
    print("Niño/a.")
elif(edad >= 12 and edad < 18):
    print("Adolescente.")
elif(edad >= 18 and edad < 30): 
    print("Adulto/a joven.")
elif(edad >= 30): 
    print("Adulto.")

#Ejercicio 5
print("Ejercicio 5")
contraseña = input("Ingrese una contraseña: ")

if(len(contraseña) >= 8 and len(contraseña) <= 12): 
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6 
from statistics import mode, median, mean
import random
print("Ejercicio 6")
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

promedio = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if(promedio > mediana and mediana > moda): 
    print("Sesgo positivo o a la derecha")
elif(promedio < mediana and mediana < moda): 
    print("Sesgo negativo o a la izquierda")
elif(promedio == mediana and mediana == moda):
    print("Sin sesgo")


#Ejercicio 7
print("Ejercicio 7")
palabra = input("Ingrese una frase o palabra: ")

if(palabra[-1].lower() in "aeiou"): 
    palabra += "!"

print(palabra)

#Ejercicio 8
print("Ejercicio 8")
nombre = input("Ingrese su nombre: ")
print("Elija un numero: \n 1. Si quiere su nombre en mayúsculas. \n 2. Si quiere su nombre en minúsculas. \n 3. Si quiere su nombre con la primera letra mayúscula.")
num: int = int(input("Ingrese una opcion: "))

if(num == 1): 
    nombre = nombre.upper()
elif(num == 2): 
    nombre = nombre.lower()
elif(num == 3): 
    nombre = nombre.capitalize()
else: 
    print("Opcion invalida.")

print(nombre)

#Ejericicio 9
print("Ejercicio 9")
magnitud: float = float(input("Ingrese la magnitud: "))

if(magnitud < 3): 
    print("Muy leve.")
elif(magnitud >= 3 and magnitud < 4): 
    print("Leve.")
elif(magnitud >= 4 and magnitud < 5): 
    print("Moderado.")
elif(magnitud >= 5 and magnitud < 6): 
    print("Fuerte.")
elif(magnitud >= 6 and magnitud < 7): 
    print("Muy fuerte.")
elif(magnitud >= 7): 
    print("Extremo.")

#Ejercicio 10 
print("Ejercicio 10")
hemisferio = input("Ingrese el hemisferio donde se encuentra N/S: ").lower()
mes = input("Ingrese el mes del año: ")
dia = int(input("Ingrese el dia del mes: "))

periodo1 = [
    ["diciembre", range(21, 31)],
    ["enero", range(1,30)],
    ["febrero", range(1,28)],
    ["marzo", range(1,20)]
]

periodo2 = [
    ["marzo", range(20,31)],
    ["abril", range(1,30)],
    ["mayo", range(1,31)],
    ["junio", range(1,20)]
]

periodo3 = [
    ["junio", range(20,31)],
    ["julio", range(1,31)],
    ["agosto", range(1,31)],
    ["septiembre", range(1,20)]
]

periodo4 = [
    ["septiembre", range(20,30)],
    ["octubre", range(1,31)],
    ["noviembre", range(1,30)],
    ["diciembre", range(1,20)]
]

periodos = [periodo1, periodo2, periodo3, periodo4]

if hemisferio == "s":
    estaciones = ["Verano", "Otoño", "Invierno", "Primavera"]
else:
    estaciones = ["Invierno", "Primavera", "Verano", "Otoño"]

for i, periodo in enumerate(periodos):
    for m, r in periodo:
        if mes == m and dia in r:
            print(estaciones[i])
            break