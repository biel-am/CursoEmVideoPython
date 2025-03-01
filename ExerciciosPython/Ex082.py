numbers = []
numbers_even = []
numbers_odd = []
while True:
    n = int(input('Digite um número inteiro: '))
    numbers.append(n)
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if not op or op not in 'S' 'N':
            print('Opção inválida, digite novamente.')
        else:
            break
    if op == 'N':
        break
for n in numbers:
    if n % 2 == 0:
        numbers_even.append(n)
    else:
        numbers_odd.append(n)
print(f'Números Gerais: {numbers}')
print(f'Números Pares: {numbers_even}')
print(f'Números Ímpares: {numbers_odd}')
