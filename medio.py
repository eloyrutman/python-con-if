a = b = c = 0
medio = " "

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

if (a <= b and a >= c) or (a >= b and a <= c):
    medio = " esta en A"
if (b <= a and b >= c) or (b >= a and b <= c):
    medio = " esta en B"
if (c <= a and c >= b) or (c >= a and c <= b):
    medio = " esta en C"

print("El medio ", medio)

