def encontrar_maximo(*args):
    # Encuentra el valor máximo entre los argumentos
    if not args:
        return None
    
    maximo = args[0]
    for numero in args:
        if numero > maximo:
            maximo = numero
    
    return maximo

# Solicitar los datos al usuario
datos_str = input("Ingresa los números separados por espacios: ")

try:
    # Convertir los strings a números flotantes
    numeros = [float(x) for x in datos_str.split()]
    
    if not numeros:
        print("Error: No ingresaste ningún número.")
    else:
        maximo = encontrar_maximo(*numeros)
        print(f"Los números ingresados son: {numeros}")
        print(f"El valor máximo es: {maximo}")
        
except ValueError:
    print("Error: Debes ingresar solo números válidos separados por espacios.")