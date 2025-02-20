n1 = int(input('Digite o valor da primeira reta: '))
n2 = int(input('Digite o valor da segunda reta: '))
n3 = int(input('Digite o valor da terceira reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Será possível formar um triângulo!')
    if n1 == n2 == n3:
        print('Tipo: Equilátero')
    elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
        print('Tipo: Isósceles')
    else:
        print('Tipo: Escaleno')
else:
    print('Não será possível formar um triângulo')
