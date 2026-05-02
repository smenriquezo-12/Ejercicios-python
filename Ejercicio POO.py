# Ejercicio POO - Clase Estudiante

class Estudiante:
    
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []   # lista vacía al inicio

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 61


# Prueba del programa
est1 = Estudiante("Sergio", "2500205", "Ingeniería")

est1.agregar_nota(70)
est1.agregar_nota(80)
est1.agregar_nota(65)

print("Nombre:", est1.nombre)
print("Carnet:", est1.carnet)
print("Carrera:", est1.carrera)
print("Notas:", est1.notas)
print("Promedio:", est1.promedio())
print("¿Aprobado?:", est1.aprobado())