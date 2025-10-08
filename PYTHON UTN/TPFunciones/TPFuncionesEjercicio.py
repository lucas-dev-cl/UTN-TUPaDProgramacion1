# Ejercicio 1
def saludar(): 
    print("Hola mundo")

saludar()

# Ejercicio 2
def saludar_usuario(nombre): 
    print(f"Hola, {nombre}")

saludar_usuario("Lucas")

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia): 
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal("Lucas", "Gallardo", 19, "Las Heras")

import math

radioValor :int = int(input("Ingrese el radio para calcular area y perimetro: "))

def calcular_area_circulo(radio):
    return  math.pi * radio ** 2


def calcular_perimetro_circulo(radio): 
    return 2 * math.pi * radio

print(f"""
Area: {calcular_area_circulo(radioValor)}
Perimetro: {calcular_perimetro_circulo(radioValor)}    
""")

# Ejercicio 5
segundosValor :int = int(input("Ingrese cantidad de segundos: "))

def segundos_a_horas(segundos): 
    horas = segundos / 3600
    return horas

print(f"La cantidad de horas son {segundos_a_horas(segundosValor)}")

# Ejercicio 6
numValor :int = int(input("Ingrese un numero: "))

def tabla_multiplicar(numero):
    for i in range(11): 
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(numValor)

# Ejercicio 7
num1 :float = float(input("Ingrese el primer número: "))
num2 :float = float(input("Ingrese el segundo número: "))  

def operaciones_basicas(a, b): 
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if(b == 0): 
        division = None
    else: 
        division = a / b

    return (suma, resta, multiplicacion, division)

res = operaciones_basicas(num1, num2)

print(f"""
suma = {res[0]}
resta = {res[1]}
multiplicacion = {res[2]}
division = {res[3] if res[3] is not None else "No se puede dividir por cero"}
""")

# Ejercicio 8
peso :float = float(input("Ingrese su peso: "))
altura :float = float(input("Ingrese su altura: "))  


def calcular_imc(peso, altura): 
    return peso / altura

print(f"Su IMC es: {calcular_imc(peso, altura)}")

# Ejercicio 9
temp_c :float= float(input("Ingrese la temperatura en grados Celsius: "))

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

temp_f = celsius_a_fahrenheit(temp_c)

print(f"{temp_c}°C equivalen a {temp_f}°F")

# Ejercicio 10
valor1 :float = float(input("Ingrese la nota 1: "))
valor2 :float = float(input("Ingrese la nota 2: "))  
valor3 :float = float(input("Ingrese la nota 3: "))

def calcular_promedio(a, b, c): 
    res = (a + b + c) / 3
    print(f"promedio: {res}")

calcular_promedio(valor1, valor2, valor3)
