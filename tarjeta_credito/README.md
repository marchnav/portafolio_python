# 💳 Tarjeta de Crédito en Python

Este proyecto implementa una clase `TarjetaCredito` en Python para simular el comportamiento de una tarjeta de crédito. Se aplican los principios de la programación orientada a objetos (POO), incluyendo encapsulamiento, atributos por defecto, métodos encadenables y manejo de instancias múltiples.

## 🧠 Objetivos

- Aplicar conceptos fundamentales de clases y objetos en Python.
- Usar atributos de instancia y valores por defecto.
- Encadenar métodos para realizar múltiples operaciones en una sola línea.
- Validar límites de crédito y aplicar intereses.
- Administrar múltiples instancias mediante un método de clase.

## 📌 Funcionalidades de la Clase

### Atributos

- `saldo_pagar`: Monto que el usuario debe actualmente. Por defecto es 0.
- `limite_credito`: Límite máximo de crédito disponible.
- `intereses`: Tasa de interés aplicada (por ejemplo, 0.02 para 2%).

### Métodos

| Método | Descripción |
|--------|-------------|
| `compra(monto)` | Realiza una compra si no supera el límite. Si excede, imprime mensaje de rechazo. |
| `pago(monto)` | Reduce el saldo pendiente de pago. |
| `cobrar_interes()` | Aplica los intereses al saldo actual. |
| `mostrar_info_tarjeta()` | Muestra el saldo pendiente en consola. |
| `mostrar_todas()` (método de clase) | Imprime la información de todas las tarjetas creadas. |




### 👨🏻‍💻Autor
**Marcelo Navarrete Y** 🚀  
🔧Desarrollador FullStack in progress ... 
🔋 Progreso: ➂➈ %
[████████░░░░░░░░░░░░░░░░░░░░░░░░░]

