# 1. Crear tupla con coordenadas
coordenadas_ciudad = (14.6349, -90.5656)

# 2. Desempaquetar en variables lat, lon
lat, lon = coordenadas_ciudad
print(f"Latitud: {lat}, Longitud: {lon}")


# 3. Función que retorna (min, max, promedio)
def calcular_estadisticas(numeros):
    if not numeros:  # validación
        return None
    
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)
    
    return (minimo, maximo, promedio)


# Uso de la función con desempaquetado (mejor que usar índices)
lista = [10, 20, 30, 40, 50]
minimo, maximo, promedio = calcular_estadisticas(lista)

print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Promedio: {promedio}")


# 4. Usar tuplas como claves de un diccionario
distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45
}

# Acceso
print("\nDistancias:")
for ciudades, distancia in distancias.items():
    origen, destino = ciudades  # desempaquetado de tupla
    print(f"{origen} -> {destino}: {distancia} km")


# 5. Intentar modificar una tupla
try:
    coordenadas_ciudad[0] = 15.0
except TypeError as e:
    print("\nError al modificar la tupla:", e)
    print("Explicación: Las tuplas son inmutables, no se pueden cambiar después de crearse.")