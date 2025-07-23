"""unit_converter.py
Conversor simple de unidades: temperatura (C/F), longitud (m/ft), moneda (USD/CLP)
Uso: ejecutar y seguir las instrucciones.
"""

def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def m_to_ft(m):
    return m * 3.28084

def ft_to_m(ft):
    return ft / 3.28084

def usd_to_clp(usd, rate=900):
    return usd * rate

def clp_to_usd(clp, rate=900):
    return clp / rate

def main():
    print("=== Conversor de Unidades ===")
    print("1. Temperatura C→F")
    print("2. Temperatura F→C")
    print("3. Metros → Pies")
    print("4. Pies → Metros")
    print("5. USD → CLP")
    print("6. CLP → USD")
    opcion = input("Selecciona una opción: ")
    try:
        if opcion == '1':
            valor = float(input("Celsius: "))
            print("Fahrenheit:", c_to_f(valor))
        elif opcion == '2':
            valor = float(input("Fahrenheit: "))
            print("Celsius:", f_to_c(valor))
        elif opcion == '3':
            valor = float(input("Metros: "))
            print("Pies:", m_to_ft(valor))
        elif opcion == '4':
            valor = float(input("Pies: "))
            print("Metros:", ft_to_m(valor))
        elif opcion == '5':
            valor = float(input("USD: "))
            print("CLP:", usd_to_clp(valor))
        elif opcion == '6':
            valor = float(input("CLP: "))
            print("USD:", clp_to_usd(valor))
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada no válida.")

if __name__ == "__main__":
    main()
