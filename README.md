Sistema de Gestión de Estudiantes
Descripción

Este proyecto es un programa desarrollado en Python que permite gestionar información de estudiantes utilizando archivos CSV.

El sistema ofrece funcionalidades completas como:

* Lectura y almacenamiento de datos
* Gestión de estudiantes (CRUD)
* Cálculo de estadísticas
* Exportación de información a formato JSON

Todo el sistema está diseñado con manejo de errores usando `try/except` para garantizar estabilidad.

Funcionalidades

Leer datos desde un archivo CSV
Convertir datos a lista de diccionarios
Buscar estudiantes por ID
Agregar nuevos estudiantes
Eliminar estudiantes existentes
Calcular estadísticas:

Promedio de notas
Mejor nota
Peor nota

Guardar cambios automáticamente en el CSV
Exportar datos a archivo JSON

---

Requisitos

Python 3.x instalado

---

Cómo ejecutar el programa

1. Clona este repositorio o descarga los archivos
2. Asegúrate de tener un archivo llamado `datos.csv` en la misma carpeta
3. Ejecuta el programa con el siguiente comando:

```bash
python main.py
```

4. Usa el menú interactivo para gestionar los estudiantes

---

Estructura del proyecto

```
gestion_estudiantes/
│
├── main.py        # Programa principal
├── datos.csv      # Base de datos de estudiantes
├── reporte.json   # Archivo exportado
└── README.md      # Documentación
```

---

Formato del archivo CSV

El archivo `datos.csv` debe tener la siguiente estructura:

```
id,nombre,edad,nota
1,Juan,20,85
2,Ana,22,90
3,Carlos,19,78
```

---

Ejemplo de uso

* Mostrar estudiantes registrados
* Buscar un estudiante por ID
* Agregar un nuevo estudiante
* Eliminar registros
* Ver estadísticas generales
* Exportar datos a JSON

---

Manejo de errores

El sistema utiliza bloques `try/except` en todas las operaciones críticas como:

* Lectura y escritura de archivos
* Entrada de datos del usuario
* Procesamiento de información

Esto evita que el programa falle ante errores inesperados.

---

Control de versiones (Git)

Ejemplo de commits recomendados:

```bash
git init
git add .
git commit -m "Versión inicial del sistema"
git commit -m "Implementación de CRUD de estudiantes"
git commit -m "Agregadas funciones de estadísticas"
git commit -m "Exportación a JSON y manejo de errores"
```

---

Autor

Proyecto académico desarrollado como parte de un Proyecto Integrador en Python.

---

Notas finales

Este proyecto puede mejorarse agregando:

* Interfaz gráfica (Tkinter o web)
* Validaciones más estrictas
* Base de datos (MySQL, SQLite)

---
