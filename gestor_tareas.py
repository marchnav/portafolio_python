    """
    gestor_tareas.py
    Pequeña aplicación CLI para gestionar tareas.

    Requisitos cubiertos:
    - Menú interactivo
    - CRUD de tareas (agregar, listar, completar, eliminar)
    - Persistencia en archivo JSON
    - Manejo de errores y validaciones
    - Uso de funciones y estructuras de datos básicas

    Autor: Marcelo Navarrete
    """
    import json
    import os
    from typing import List, Dict

    DATA_FILE = "tareas.json"


    # ─────────────────────────── Persistencia ────────────────────────────
    def cargar_tareas() -> List[Dict]:
        if not os.path.exists(DATA_FILE):
            return []
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            # Archivo corrupto o inaccesible → empezar de cero
            return []


    def guardar_tareas(tareas: List[Dict]):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tareas, file, indent=2, ensure_ascii=False)


    # ───────────────────────────── Operaciones ────────────────────────────
    def agregar_tarea(tareas: List[Dict]):
        descripcion = input("Descripción de la tarea: ").strip()
        if descripcion:
            tarea = {"descripcion": descripcion, "completada": False}
            tareas.append(tarea)
            guardar_tareas(tareas)
            print("✓ Tarea agregada.
")
        else:
            print("⚠️  Descripción vacía. No se agregó la tarea.
")


    def listar_tareas(tareas: List[Dict]):
        if not tareas:
            print("No hay tareas registradas.
")
            return
        print("\n--- Lista de Tareas ---")
        for idx, tarea in enumerate(tareas, start=1):
            estado = "✔ Completada" if tarea["completada"] else "Pendiente"
            print(f"{idx}. [{estado}] {tarea['descripcion']}")
        print()  # Línea en blanco


    def marcar_completada(tareas: List[Dict]):
        listar_tareas(tareas)
        if not tareas:
            return
        try:
            num = int(input("Número de tarea a marcar como completada: "))
            if 1 <= num <= len(tareas):
                tareas[num - 1]["completada"] = True
                guardar_tareas(tareas)
                print("✓ Tarea marcada como completada.\n")
            else:
                print("⚠️  Número fuera de rango.\n")
        except ValueError:
            print("⚠️  Entrada inválida. Debes ingresar un número.\n")


    def eliminar_tarea(tareas: List[Dict]):
        listar_tareas(tareas)
        if not tareas:
            return
        try:
            num = int(input("Número de tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                tarea_borrada = tareas.pop(num - 1)
                guardar_tareas(tareas)
                print(f"✓ Tarea '{tarea_borrada['descripcion']}' eliminada.\n")
            else:
                print("⚠️  Número fuera de rango.\n")
        except ValueError:
            print("⚠️  Entrada inválida. Debes ingresar un número.\n")


    # ────────────────────────────── Menú CLI ──────────────────────────────
    def menu():
        tareas = cargar_tareas()
        opciones = {
            "1": agregar_tarea,
            "2": listar_tareas,
            "3": marcar_completada,
            "4": eliminar_tarea,
            "5": lambda _: exit("¡Hasta luego! 👋")
        }
        while True:
            print(textwrap.dedent("""
                --- Gestor de Tareas ---
                1. Agregar tarea
                2. Ver tareas
                3. Marcar tarea como completada
                4. Eliminar tarea
                5. Salir
            """))
            eleccion = input("Elige una opción: ").strip()
            accion = opciones.get(eleccion)
            if accion:
                accion(tareas)
            else:
                print("⚠️  Opción no válida. Intenta de nuevo.\n")


    if __name__ == "__main__":
        import textwrap
        menu()
