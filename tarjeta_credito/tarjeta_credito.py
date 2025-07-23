
class TarjetaCredito:
    tarjetas = []  # lista para almacenar todas las instancias

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        # registrar instancia
        TarjetaCredito.tarjetas.append(self)

    # Métodos que devuelven self para permitir encadenamiento
    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self

    def pago(self, monto):
        self.saldo_pagar = max(self.saldo_pagar - monto, 0)
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    # BONUS: método de clase para mostrar todas las tarjetas
    @classmethod
    def mostrar_todas(cls):
        print("\n--- Información de todas las tarjetas ---")
        for idx, tarjeta in enumerate(cls.tarjetas, start=1):
            print(f"Tarjeta {idx}:")
            tarjeta.mostrar_info_tarjeta()
        print("-----------------------------------------\n")


if __name__ == "__main__":
    # Crear 3 tarjetas
    tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
    tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.03)
    tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.05)

    # Tarjeta 1: 2 compras, 1 pago, intereses, mostrar info
    tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

    # Tarjeta 2: 3 compras, 2 pagos, intereses, mostrar info
    tarjeta2.compra(300).compra(400).compra(250).pago(200).pago(150).cobrar_interes().mostrar_info_tarjeta()

    # Tarjeta 3: 5 compras (exceder límite), mostrar info
    tarjeta3.compra(100).compra(150).compra(120).compra(90).compra(80).mostrar_info_tarjeta()

    # BONUS: Mostrar todas las tarjetas
    TarjetaCredito.mostrar_todas()
