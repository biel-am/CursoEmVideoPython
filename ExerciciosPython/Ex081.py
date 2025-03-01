numbers = []
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
numbers_reverse_order = numbers[:]
numbers_reverse_order.sort(reverse=True)
print(f'Quantidade de números digitados: {len(numbers)}')
print(f'Lista dos valores em ordem descrescente: {numbers_reverse_order}')
if 5 in numbers:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 NÃO está na lista.')
