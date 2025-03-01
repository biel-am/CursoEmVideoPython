numbers = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in numbers:
        numbers.append(n)
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if not op or op not in 'S' 'N':
            print('Opção inválida, digite novamente.')
        else:
            break
    if op == 'N':
        break
numbers.sort()
print(f'Os valores únicos digitados foram: {numbers}')
