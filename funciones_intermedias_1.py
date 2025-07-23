"""
funciones_intermedias_1.py
Autor: Marcelo Navarrete
Descripción:
- Actualiza valores en diccionarios y listas.
- Define funciones reutilizables para recorrer y mostrar estructuras.
"""

# ─── 1. Actualizar valores ──────────────────────────────────────────────

def actualizar_datos():
    matriz = [[10, 15, 20], [3, 7, 14]]
    matriz[1][0] = 6

    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"}
    ]
    cantantes[0]["nombre"] = "Enrique Martin Morales"

    ciudades = {
        "México": ["Ciudad de México", "Guadalajara", "Cancún"],
        "Chile": ["Santiago", "Concepción", "Viña del Mar"]
    }
    ciudades["México"][2] = "Monterrey"

    coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]
    coordenadas[0]["latitud"] = 9.9355431

    return matriz, cantantes, ciudades, coordenadas


# ─── 2. Iterar lista de diccionarios ─────────────────────────────────────

def iterar_diccionario(lista):
    for item in lista:
        salida = ", ".join([f"{clave} - {valor}" for clave, valor in item.items()])
        print(salida)


# ─── 3. Obtener valores de una clave ─────────────────────────────────────

def iterar_diccionario2(llave, lista):
    for item in lista:
        if llave in item:
            print(item[llave])


# ─── 4. Recorrer diccionario con listas ──────────────────────────────────

def imprimir_informacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)
        print()


# ─── Pruebas de ejemplo ──────────────────────────────────────────────────

if __name__ == "__main__":
    # 1. Actualización
    matriz, cantantes, ciudades, coordenadas = actualizar_datos()
    print("Matriz:", matriz)
    print("Ciudades:", ciudades)
    print("Coordenadas:", coordenadas)
    print()

    # Nuevos cantantes para pruebas 2 y 3
    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"},
        {"nombre": "José José", "pais": "México"},
        {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
    ]

    # 2. Iterar diccionario
    iterar_diccionario(cantantes)
    print()

    # 3. Obtener claves
    print("Nombres:")
    iterar_diccionario2("nombre", cantantes)
    print("Paises:")
    iterar_diccionario2("pais", cantantes)
    print()

    # 4. Diccionario con listas
    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }
    imprimir_informacion(costa_rica)
