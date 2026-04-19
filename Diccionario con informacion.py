def crear_diccionario(nombre, edad, ciudad, lenguaje):
    if not nombre or not ciudad or not lenguaje:
        raise ValueError("Nombre, ciudad y lenguaje no pueden estar vacíos")
    
    if not isinstance(edad, int) or edad <= 0:
        raise ValueError("La edad debe ser un número positivo")
    
    return {
        'nombre': nombre,
        'edad': edad,
        'ciudad': ciudad,
        'lenguaje_favorito': lenguaje
    }


def agregar_universidad(diccionario, universidad):
    diccionario['universidad'] = universidad


def modificar_edad(diccionario, nueva_edad):
    if isinstance(nueva_edad, int) and nueva_edad > 0:
        diccionario['edad'] = nueva_edad
    else:
        print("Edad inválida")


def imprimir_diccionario(diccionario):
    print("\n--- Información ---")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


def verificar_email(diccionario):
    if 'email' in diccionario:
        print("El email existe")
    else:
        print("El email no existe")


def obtener_telefono(diccionario):
    telefono = diccionario.get('telefono', 'No disponible')
    print(f"Teléfono: {telefono}")


# Programa principal
def main():
    try:
        mi_info = crear_diccionario("Sergio Enriquez", 23, "Escuintla", "Python")
        agregar_universidad(mi_info, "USPG")
        modificar_edad(mi_info, 31)

        imprimir_diccionario(mi_info)
        verificar_email(mi_info)
        obtener_telefono(mi_info)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()