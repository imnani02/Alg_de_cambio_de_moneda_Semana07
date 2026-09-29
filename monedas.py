def calcular_cambio(monto):
    monedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]
    pendiente = monto
    cantidades = []

    for moneda in monedas:
        cantidad = int(pendiente // moneda)

        cantidades.append((moneda, cantidad))

        pendiente = round(pendiente - cantidad * moneda, 2)

    return cantidades, pendiente


monto = float(input("Ingrese el monto a pagar: S/ "))

resultado, pendiente = calcular_cambio(monto)

print("\n===== DETALLE DEL PAGO =====")
print("Denominación   Cantidad")

for moneda, cantidad in resultado:
    if cantidad > 0:
        print(f"S/{moneda:<13} {cantidad}")

print("----------------------------")
print(f"Pendiente: S/{pendiente:.2f}")