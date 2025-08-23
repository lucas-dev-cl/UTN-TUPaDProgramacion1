# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre.capitalize()}!")

# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

print(f"Soy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {residencia.capitalize()}")

# Ejercicio 4
import math

radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

# Ejercicio 5
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} equivalen a: {horas} horas")

# Ejercicio 6
num = int(input("Ingrese un numero: "))

for i in range(11): 
    print(f"{num} x {i} = {num * i}")

# Ejercicio 7
while(True): 
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))

    if(num1 == 0 or num2 == 0): 
        print("El primer valor es invalido.")
    else:
        break

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

#Ejercicio 8
peso = float(input("Ingrese su peso (en kg): "))
altura = float(input("Ingrese su altura (en m)"))

print(f"Su IMC es: {peso / (altura ** 2)}")

# Ejercicio 9 
celsius = float(input("Ingrese valor en celsius: "))

print(f"Temperatura en fahrenheit: {9/5 * celsius + 32}")

# Ejercicio 10
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es de: {promedio}")