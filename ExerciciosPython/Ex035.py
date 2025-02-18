n1 = int(input('Digite o valor da primeira reta: '))
n2 = int(input('Digite o valor da segunda reta: '))
n3 = int(input('Digite o valor da terceira reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Será possível formar um triângulo!')
else:
    print('Não será possível formar um triângulo')
