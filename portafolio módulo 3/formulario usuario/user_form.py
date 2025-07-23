"""user_form.py
Formulario en consola que solicita datos y los muestra.
"""
def main():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura (m): "))
    estudiante = input("¿Eres estudiante? (s/n): ").lower() == 's'
    print(f"\nResumen:\nNombre: {nombre}\nEdad: {edad}\nAltura: {altura} m\nEstudiante: {estudiante}")
if __name__ == "__main__":
    main()
