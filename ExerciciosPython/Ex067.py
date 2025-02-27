while True:
    print('-'*15)
    print(f'{"TABUADA":^15}')
    print('-' * 15)
    n = int(input('Digite um número inteiro (número negativo para encerrar): '))
    if n < 0:
        print('Programa encerrado com sucesso.')
        break
    else:
        for c in range(1, 11):
            print(f'{c} * {n} = {c*n}')
