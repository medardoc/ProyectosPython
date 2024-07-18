#gestor_tareas.py

class GestorTareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            print("Lista de tareas.")
            for i, tarea in enumerate(self.tareas, 1):
              print(f"{i}. {tarea}")

if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. salir")
   
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nueva_tarea = input("Ingrese la nueva tarea: ")
        gestor.agregar_tarea(nueva_tarea)
    elif opcion == "2":
        gestor.mostrar_tareas()
    elif opcion == "3":
        breakpoint
    else:
        print("Opción no valida. Intente de nuevo. ")