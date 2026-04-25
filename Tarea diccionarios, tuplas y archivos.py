import csv
import json

RUTA_CSV = "datos.csv"
RUTA_JSON = "reporte.json"

# -------------------------------
# 📁 ARCHIVO (CSV / JSON)
# -------------------------------

def leer_csv(ruta):
    estudiantes = []
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila['nota'] = float(fila['nota'])
                    estudiantes.append(fila)
                except:
                    continue
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo.")
    except Exception as e:
        print(f"Error al leer CSV: {e}")
    return estudiantes


def guardar_csv(ruta, estudiantes):
    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ['id', 'nombre', 'edad', 'nota']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(estudiantes)
    except Exception as e:
        print(f"Error al guardar CSV: {e}")


def exportar_json(ruta, datos):
    try:
        with open(ruta, mode='w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)
    except Exception as e:
        print(f"Error al exportar JSON: {e}")


# -------------------------------
# 👨‍🎓 CRUD ESTUDIANTES
# -------------------------------

def buscar_estudiante(estudiantes, id_buscar):
    try:
        for est in estudiantes:
            if est['id'] == id_buscar:
                return est
    except Exception as e:
        print(f"Error al buscar: {e}")
    return None


def agregar_estudiante(estudiantes):
    try:
        nuevo = {
            "id": input("ID: "),
            "nombre": input("Nombre: "),
            "edad": input("Edad: "),
            "nota": float(input("Nota: "))
        }
        estudiantes.append(nuevo)
        print("✅ Estudiante agregado")
    except ValueError:
        print("❌ La nota debe ser un número")
    except Exception as e:
        print(f"Error al agregar: {e}")


def eliminar_estudiante(estudiantes, id_eliminar):
    try:
        nueva_lista = [est for est in estudiantes if est['id'] != id_eliminar]
        if len(nueva_lista) == len(estudiantes):
            print("❌ No se encontró el estudiante")
        else:
            print("✅ Estudiante eliminado")
        return nueva_lista
    except Exception as e:
        print(f"Error al eliminar: {e}")
        return estudiantes


# -------------------------------
# 📊 ESTADÍSTICAS
# -------------------------------

def calcular_promedio(estudiantes):
    try:
        if not estudiantes:
            return 0
        return sum(e['nota'] for e in estudiantes) / len(estudiantes)
    except Exception as e:
        print(f"Error promedio: {e}")
        return 0


def mejor_nota(estudiantes):
    try:
        return max(estudiantes, key=lambda x: x['nota'])
    except Exception as e:
        print(f"Error mejor nota: {e}")
        return None


def peor_nota(estudiantes):
    try:
        return min(estudiantes, key=lambda x: x['nota'])
    except Exception as e:
        print(f"Error peor nota: {e}")
        return None


# -------------------------------
# 📋 MENÚ
# -------------------------------

def menu():
    print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
    print("1. Mostrar estudiantes")
    print("2. Buscar estudiante")
    print("3. Agregar estudiante")
    print("4. Eliminar estudiante")
    print("5. Ver estadísticas")
    print("6. Exportar a JSON")
    print("7. Salir")


# -------------------------------
# 🚀 MAIN
# -------------------------------

def main():
    estudiantes = leer_csv(RUTA_CSV)

    while True:
        menu()
        opcion = input("Seleccione opción: ")

        try:
            if opcion == "1":
                if not estudiantes:
                    print("No hay estudiantes")
                for e in estudiantes:
                    print(e)

            elif opcion == "2":
                id_buscar = input("ID: ")
                est = buscar_estudiante(estudiantes, id_buscar)
                print(est if est else "❌ No encontrado")

            elif opcion == "3":
                agregar_estudiante(estudiantes)

            elif opcion == "4":
                id_eliminar = input("ID: ")
                estudiantes = eliminar_estudiante(estudiantes, id_eliminar)

            elif opcion == "5":
                print(f"Promedio: {calcular_promedio(estudiantes):.2f}")
                print("Mejor:", mejor_nota(estudiantes))
                print("Peor:", peor_nota(estudiantes))

            elif opcion == "6":
                exportar_json(RUTA_JSON, estudiantes)
                print("✅ Exportado a JSON")

            elif opcion == "7":
                guardar_csv(RUTA_CSV, estudiantes)
                print("💾 Datos guardados. Saliendo...")
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"Error general: {e}")


if __name__ == "__main__":
    main()