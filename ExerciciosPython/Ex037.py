num = int(input('Digite um número inteiro: '))
print(""""Escolha uma das opções de conversão à seguir:
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal""")
op = int(input('Digite a opção desejada: '))
if op == 1:
    print(f'O número {num} convertido para binário é igual {bin(num)}')
elif op == 2:
    print(f'O número {num} convertido para octal é igual {oct(num)}')
elif op == 3:
    print(f'O número {num} convertido para hexadecimal é igual {hex(num)}')
else:
    print('A opção digitada, é inválida')
