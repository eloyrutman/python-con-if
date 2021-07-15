a = b = c = 0
mayor = medio = menor = " "

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

if (a >= b) and (a >= c):
    mayor = a
if (a <= b) and (a <= c):
    menor = a
if (a != mayor) and (a != menor):
     medio = a

if (b >= a) and (b >= c):
    mayor = b
if (b <= a) and (b <= c):
    menor = b
if (b != mayor) and (b != menor):
    medio = b

if (c >= a) and (c >= b):
    mayor = c
if (c <= a) and (c <= b):
    menor = c
if (c != mayor) and (c != menor):
     medio = c


print( menor , medio , mayor )
    


    
