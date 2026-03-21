import math

def es_primo(n):
    # Retorna True si n es primo, False en caso contrario
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

# Programa principal
numero_str = input("Ingresa un número para verificar si es primo: ")

try:
    numero = int(numero_str)
    resultado = es_primo(numero)
    
    # Mostrar resultado
    print(f"El número {numero} es primo: {resultado}")
    
    # También podemos retornar el valor si se necesita
    
    
except ValueError:
    print("Error: Debes ingresar un número entero válido.")