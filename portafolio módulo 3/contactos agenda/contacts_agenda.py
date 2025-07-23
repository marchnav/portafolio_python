"""Simple agenda usando diccionario"""
agenda = {}
def agregar():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
def ver():
    for nombre, tel in agenda.items():
        print(nombre, "->", tel)
def buscar():
    nombre = input("Nombre a buscar: ")
    print("Teléfono:", agenda.get(nombre, "No encontrado"))
def main():
    while True:
        print("1. Agregar 2. Ver 3. Buscar 4. Salir")
        op = input("> ")
        if op=='1': agregar()
        elif op=='2': ver()
        elif op=='3': buscar()
        elif op=='4': break
        else: print("Opción inválida")
if __name__ == "__main__":
    main()
