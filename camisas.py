camisas = 0
camisas1 = 0
camisas2 = 0

camisas = int(input("Camisas compradas: "))

if camisas <= 3:
    camisas2 = camisas * 12
    print("Cantidad a Pagar: ", camisas2)
    
else:
    camisas1 = camisas * 10
    print("Cantidad a Pagar: ", camisas1)
