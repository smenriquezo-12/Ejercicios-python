for num in range(1, 13):
    print(f"\n--- Tabla del {num} ---")
    for i in range(1, 13):
        resultado = num * i
        print(f"{num} * {i:2d} = {resultado:3d}")
    print("-" * 20)