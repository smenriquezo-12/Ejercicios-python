tareas = []
tareasc = []

while True:
    print("--- Lista de tareas ---")
    print()
    print("1. Agregar tarea")
    print("2. Ver tarea")
    print("3. Eliminar tarea")
    print("4. Marcar tarea completada")
    print("5. Ver tareas completadas")
    print("6. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append(tarea)
        print("Agregada")

    elif opcion == "2":
        for i, t in enumerate(tareas, 1):
            print(f" {i}.{t}")
    
    elif opcion == "3":
        idx = int(input("Indique el numero de la tarea a elimar: "))
        tareas.pop(idx-1)

    elif opcion == "4":
        tareac = input ("Indica el Numero de la tarea realizada: ")
        tareasc.append(tareac)
        print("Se identifico la tarea completada")

    elif opcion == "5":
        for s, a in enumerate(tareasc, 1):
            print(f" {s}.{a}")
    
    
    elif opcion == "6":
        break