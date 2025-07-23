"""
operaciones_diccionarios_listas.py
Autor: Marcelo Navarrete
Descripción:
    1) Actualiza estructuras de datos según indicaciones.
    2) Recorre lista de diccionarios `cantantes` y muestra nombre‑país.
    3) Extrae valores de claves específicas.
    4) Recorre diccionario `costa_rica` mostrando conteo y elementos.
"""

def actualizar_datos():
    # 1. Matriz
    matriz = [[10, 15, 20], [3, 7, 14]]
    matriz[1][0] = 6  # Cambiar 3 por 6

    # 2. Cantantes
    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"}
    ]
    cantantes[0]["nombre"] = "Enrique Martin Morales"

    # 3. Ciudades
    ciudades = {
        "México": ["Ciudad de México", "Guadalajara", "Cancún"],
        "Chile": ["Santiago", "Concepción", "Viña del Mar"]
    }
    ciudades["México"][2] = "Monterrey"

    # 4. Coordenadas
    coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]
    coordenadas[0]["latitud"] = 9.9355431

    return matriz, cantantes, ciudades, coordenadas


def recorrer_cantantes(cantantes):
    print("== Cantantes ==")
    for cantante in cantantes:
        print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")
    print()


def obtener_valores_clave(cantantes, clave):
    return [cantante[clave] for cantante in cantantes]


def recorrer_costa_rica():
    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }

    print("== Costa Rica ==")
    for clave, lista in costa_rica.items():
        print(f"{len(lista)} elementos en {clave.upper()}")
        for item in lista:
            print(item)
        print()


if __name__ == "__main__":
    matriz, cantantes, ciudades, coordenadas = actualizar_datos()

    print("== Estructuras actualizadas ==")
    print("Matriz:", matriz)
    print("Ciudades:", ciudades)
    print("Coordenadas:", coordenadas)
    print()

    # 2) Recorrer cantantes
    recorrer_cantantes(cantantes)

    # 3) Obtener valores específicos
    nombres = obtener_valores_clave(cantantes, "nombre")
    paises = obtener_valores_clave(cantantes, "pais")
    print("Nombres:", nombres)
    print("Paises:", paises)
    print()

    # 4) Recorrer Costa Rica
    recorrer_costa_rica()
