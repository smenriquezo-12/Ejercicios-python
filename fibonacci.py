def fibonacci(n):
    # Validar que sea positivo
    if n <= 0:
        return None
    
    # Casos base
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Calcular Fibonacci usando ciclo
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    
    return b

# Solicitar el número al usuario
numero_str = input("Ingresa la posición para calcular el número de Fibonacci: ")

try:
    numero = int(numero_str)
    
    # Validar si el número es menor o igual a 0
    if numero <= 0:
        print("ingrese valores positivos")
    else:
        resultado = fibonacci(numero)
        print(f"El número de Fibonacci en la posición {numero} es: {resultado}")
        
except ValueError:
    print("Error: Debes ingresar un número entero válido.")