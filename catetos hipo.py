from math import sqrt

x1 = y1 = 0.0; x2 = y2 = 0.0
x3 = y3 = 0.0
hipo = " "
rectan = esca = isos = " "

x1 = float(input("Valor de X1: "))
y1 = float(input("Valor de Y1: "))
x2 = float(input("Valor de X2: "))
y2 = float(input("Valor de Y2: "))
x3 = float(input("Valor de X3: "))
y3 = float(input("Valor de Y3: "))

v1 = x3 - x2
v2 = y3 - y2
cateto1 = sqrt( (v2)**2 + (v1)**2 )
v3 = x2 - x1
v4 = y2 - y1
cateto2 = sqrt( (v3)**2 + (v4)**2 )
v5 = x3 - x1
v6 = y3 - y1
cateto3 = sqrt( (v6)**2 + (v5)**2 )

num = cateto1
num2= cateto2
num3 =cateto3

if cateto1 >= cateto2 and cateto1 >= cateto3:
    hipo = cateto1
if cateto2 >= cateto1 and cateto2 >= cateto3:
    hipo = cateto2
if cateto3 >= cateto1 and cateto3 >= cateto2:
    hipo = cateto3

if  (hipo >= num) or (hipo >= num2) or (hipo >= num3):
    rectan = "Triangulo Rectangulo"
if (cateto1 == cateto2) or (cateto2 == cateto3) or (cateto1 == cateto3):
    rectan = "Triangulo Rectangulo Isosceles"
elif (cateto1 != cateto2) or (cateto2 != cateto3) or (cateto1 != cateto3):
    rectan = "Triangulo Rectangulo Escaleno"
else:
    rectan = "No es un Triangulo Rectangulo"

print("Hipotenusa: ", hipo , "Cateto 1: " , cateto1 ,"Cateto 2" , cateto2 ,"Cateto 3: " , cateto3 , rectan)
