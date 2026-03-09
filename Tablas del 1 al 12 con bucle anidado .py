# Tablas de multiplicar del 1 al 12 con bucle anidado

for num in range(1, 13):  # Bucle externo: número de la tabla (1-12)
    print(f"\n--- tabla del {num} ---")
    
    for i in range(1, 13):  # Bucle interno: multiplicadores (1-12)
        resultado = num * i
        print(f"{num} x {i:2d} = {resultado:3d}")