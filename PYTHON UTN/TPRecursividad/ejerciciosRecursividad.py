# Funciones recursivas
def factorial(n):
    if(n == 0): 
        return 1
    else: 
        return n * factorial(n - 1) 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def potencia(b, e):
    if(e == 0): 
        return 1
    else: 
        return b * potencia(b, e - 1)

def decimal_a_binario(n):
    if n == 0:                      
        return "0"
    if n == 1:                      
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
def contar_bloques(n):
    if n == 1:           
        return 1
    else:
        return n + contar_bloques(n - 1)

def es_palindromo(palabra):
    # Si la palabra tiene una longitud de 0 o 1 entonces es palindromo
    if len(palabra) <= 1:
        return True
    
    # Si el primer elemento y el ultimo son iguales, entonces no es palindromo
    if palabra[0] != palabra[-1]:
        return False

    # Comparamos lo que queda en el medio
    return es_palindromo(palabra[1:-1])

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def contar_digito(numero, digito):
    if numero == 0:
        return 0

    ultimo = numero % 10
    resto = numero // 10

    # Si coincide, sumamos 1
    if ultimo == digito:                 
        return 1 + contar_digito(resto, digito)
    # Si no coincide, sumamos 0
    else:
        return contar_digito(resto, digito)

# Validaciones
def validar_numero(str): 
    while True: 
        numIngresado = input(str)

        if(not numIngresado.isdigit()): 
            print("Ingrese un numero valido.")
        else: 
            return int(numIngresado)
        
def validar_digito(str): 
    while True: 
        num = input(str)
        
        if num.isdigit() and 0 <= int(num) <= 9:
            return int(num)
        else:
            print("Ingrese un dígito válido (0-9).")


# Ejercicio 1
print("==== Ejercicio 1 ====")
numIngresado :str = validar_numero("Ingrese un valor para realizar un factorial: ")

print("==== Factoriales ====")
for i in range(numIngresado): 
    print(f"Factorial del numero {i + 1} = {factorial(i + 1)}")

# Ejercicio 2
print("==== Ejercicio 2 ====")
# Pedir al usuario una posición
pos = validar_numero("Ingresa la posición hasta donde quieres ver la serie: ")

print("==== Serie de Fibonacci ====")
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")

# Ejercicio 3
print("==== Ejercicio 3 ====")

b = validar_numero("Ingresa la base: ")
e = validar_numero("Ingresa el exponente: ")

print("==== Potencia ====")
print(f"{b} ^ {e} = {potencia(b, e)}")

# Ejercicio 4 
print("==== Ejercicio 4 ====")

num = validar_numero("Ingrese un numero decimal: ")
print(f"El número {num} en binario es {decimal_a_binario(num)}")

# Ejercicio 5
print("==== Ejercicio 5 ====")
palabra = input("Ingrese una palabra: ")

if es_palindromo(palabra):
    print("Es palíndromo")
else:
    print("No es palíndromo")

# Ejercicio 6
print("==== Ejercicio 6 ====")
num = validar_numero("Ingrese un numero decimal: ")
print("==== Suma de los digitos ====")
print(suma_digitos(num))

# Ejercicio 7 
print("==== Ejercicio 7 ====")
num = validar_numero("Ingrese un numero de bloques: ")

print("==== Numero de bloques que se necesitaron ====")
print(contar_bloques(num))

# Ejercicio 8
print("==== Ejercicio 7 ====")
num = validar_numero("Ingrese un numero: ")
dig = validar_digito("Ingrese un digito: ")

print(contar_digito(num, dig))