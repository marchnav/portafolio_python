def area_cuadrado(l): return l**2
def area_rectangulo(b,h): return b*h
def area_circulo(r,pi=3.1416): return pi*r**2
def main():
    print("1 Cuadrado 2 Rectángulo 3 Círculo")
    op = input("Figura: ")
    if op=='1':
        l=float(input("Lado: "))
        print("Área:", area_cuadrado(l))
    elif op=='2':
        b=float(input("Base: "))
        h=float(input("Altura: "))
        print("Área:", area_rectangulo(b,h))
    elif op=='3':
        r=float(input("Radio: "))
        print("Área:", area_circulo(r))
    else:
        print("Opción no válida")
if __name__ == "__main__":
    main()
