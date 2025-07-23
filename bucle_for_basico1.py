
"""
bucle_for_basico1.py
Autor: Marcelo Navarrete
Descripción: colección de bucles for que resuelven varios ejercicios.
"""

def ejercicio_1_basico():
    """Imprime todos los números del 0 al 100."""
    print("Ejercicio 1: Básico (0‑100)")
    for num in range(101):
        print(num)
    print("-" * 30)

def ejercicio_2_multiplos_de_2():
    """Imprime los múltiplos de 2 entre 2 y 500."""
    print("Ejercicio 2: Múltiplos de 2 (2‑500)")
    for num in range(2, 501, 2):
        print(num)
    print("-" * 30)

def ejercicio_3_contando_vanilla_ice():
    """
    Imprime 1‑100;
    - 'ice ice' si divisible por 5
    - 'baby'    si divisible por 10
    """
    print("Ejercicio 3: Contando Vanilla Ice")
    for num in range(1, 101):
        if num % 10 == 0:
            print("baby")
        elif num % 5 == 0:
            print("ice ice")
        else:
            print(num)
    print("-" * 30)

def ejercicio_4_numero_gigante():
    """Suma los números pares de 0 a 500,000 e imprime el total."""
    total = sum(range(0, 500_001, 2))
    print("Ejercicio 4: Número gigante a la vista")
    print(f"Total pares 0‑500000: {total}")
    print("-" * 30)

def ejercicio_5_regresame_al_3():
    """Cuenta regresiva de 2024 a positivos, de 3 en 3."""
    print("Ejercicio 5: Regresame al 3")
    for num in range(2024, 0, -3):
        print(num)
    print("-" * 30)

def ejercicio_6_contador_dinamico(num_inicial: int, num_final: int, multiplo: int):
    """
    Imprime números entre num_inicial y num_final (incluidos)
    que son múltiplos de 'multiplo'.
    """
    print("Ejercicio 6: Contador dinámico")
    for num in range(num_inicial, num_final + 1):
        if num % multiplo == 0:
            print(num)
    print("-" * 30)

# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Puedes comentar/descomentar las llamadas que necesites.
    ejercicio_1_basico()
    ejercicio_2_multiplos_de_2()
    ejercicio_3_contando_vanilla_ice()
    ejercicio_4_numero_gigante()
    ejercicio_5_regresame_al_3()

    # Valores de ejemplo para el ejercicio 6
    ejercicio_6_contador_dinamico(num_inicial=3, num_final=10, multiplo=2)
