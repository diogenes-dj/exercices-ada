'''
Algumas situações requerem que os dados sejam recebidos diretamente 
pelo usuário como parte da execução do programa. Isso pode ser feito 
com a função input(). No entanto, esta função sempre retorna os valores 
em string. Assim, se os dados esperados do usuário forem numéricos, é importante 
realizar a conversão dos tipos de dados para que eles possam ser processados.

Levando em consideração que o usuário pode entregar qualquer número como input, o 'XXX' 
no código acima deve ser substituído por qual elemento?

num1 = XXX

dobro = 2*num1

print("O dobro do número digitado é:", dobro)

'''

num1 = float(input("Digite um número a seguir: "))

dobro = 2*num1

print("O dobro do número digitado é:", dobro)