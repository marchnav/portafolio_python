"""
Calcula el descuento total de una compra.
"""

def obtener_descuento(cantidad_productos: int,
                      compras_previas: int,
                      monto_total: float,
                      dia_especial: bool) -> float:
    """
    Devuelve el porcentaje de descuento (0‒30).
    """
    descuento = 0.0

    # ─── Condiciones principales ──────────────────────────────────────────────
    if cantidad_productos > 10:
        descuento += 10        # 10 %

    if compras_previas > 5:
        descuento += 5         # +5 %

    if monto_total > 500:
        descuento += 7         # +7 %

    if dia_especial:
        descuento += 15        # +15 %

    # ─── Límite máximo ────────────────────────────────────────────────────────
    if descuento > 30:
        descuento = 30

    return descuento


# ─── Ejemplo de uso ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Datos de prueba (puedes cambiarlos para probar casos borde)
    productos       = 12       # >10  → 10 %
    compras_previas = 6        # >5   → +5 %
    monto           = 550.0    # >500 → +7 %
    promo_dia       = True     # True → +15 %

    total_descuento = obtener_descuento(productos, compras_previas,
                                        monto, promo_dia)

    print(f"Descuento aplicado: {total_descuento:.0f}%")
