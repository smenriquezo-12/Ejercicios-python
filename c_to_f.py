def celsius_a_fahrenheit(celsius):
    # Convierte Celsius a Fahrenheit
    return (celsius * 9/5) + 32

# Solicitar la temperatura al usuario
temperatura_str = input("Ingresa la temperatura en Celsius: ")

try:
    celsius = float(temperatura_str)
    resultado = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivale a {resultado:.2f}°F")
        
except ValueError:
    print("Error: Debes ingresar un número válido.")