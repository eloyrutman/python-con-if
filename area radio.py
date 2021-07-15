radio1 = radio2 = x = y = 0.0
area = " "

x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

radio1 = x**2 + y**2
radio2 = (x-2)**2 + y**2

if radio1 <=4:
    area = " area I"
elif radio2 <=4:
    area = " area II"
elif radio1 == radio2:
    area = " I y II"
else:
    area = " fuera de las areas"

print("El punto esta",area)
print("Fin del programa")
