#REAL d

print("Braskem | Tipos de Polietileno (PE)")

print("Digite a densidade do polietileno,em g/cm^3: ")
d = float(input())


if d > 0.93:
    print("Polietileno de Alta Densidade (PEAD)")
else:
    print("Polietileno de Baixa Densidade (PEBD)")

'''
x = 1
y = 1

while x < 5:
    if x % 2 == 0:
        y = y * x
    else:
        y = y + x
    x = x + 1

print(y,x)
'''