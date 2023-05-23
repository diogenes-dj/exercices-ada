#"O maior número entre os três informados é par?",
# (ou seja, o programa exibe, através de um booleano,
# se o maior entre os três números informados é par).

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:

  resposta = a % 2 == 0

elif b > a and b > c:

  resposta = b % 2 == 0

else:

  resposta = c % 2 == 0

print('O maior número entre os três informados é par? A resposta é:', resposta)
if resposta:

  print("Sim!!!")

else:

  print("Não!!!")