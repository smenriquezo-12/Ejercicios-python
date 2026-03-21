def factorial(n):
    # Validar que sea positivo
    if n <= 0:
        return None
    
    # Caso base
    if n == 1:
        return 1
    
    # Calcular factorial usando ciclo
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado

# Solicitar el número al usuario
numero_str = input("Ingresa un número para calcular su factorial: ")

try:
    numero = int(numero_str)
    resultado = factorial(numero)
    
    if resultado is None:
        print("ingrese valores positivos")
    else:
        print(f"El factorial de {numero} es: {resultado}")
        
except ValueError:
    print("Error: Debes ingresar un número entero válido.")