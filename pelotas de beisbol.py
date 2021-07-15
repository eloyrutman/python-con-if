cantidad = 0
pago = 0.0
descuento = 0.0
total = 0.0

cantidad = int(input("Pelotas compradas: "))

pago = cantidad * 10

if cantidad >= 3:
    total = pago - descuento
    descuento = cantidad + 0.125
    print("Total a pagar por la compra: ", total)

if cantidad <= 3:
    print("Total a pagar por la compra: ", pago)
    
