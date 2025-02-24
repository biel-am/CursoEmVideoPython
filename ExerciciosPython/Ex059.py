while True:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite um número inteiro: '))
    while True:
        print('Escolha uma das opções abaixo:')
        print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa""")
        while True:
            op = int(input('Digite a opção desejada: '))
            if not 0 < op < 6:
                print('Opção inválida, digite novamente.')
            else:
                break
        if op == 1:
            print(f'A soma entre os números {n1} e {n2}, é igual a {n1+n2}')
        if op == 2:
            print(f'O produto entre os números {n1} e {n2}, é igual a {n1*n2}')
        if op == 3:
            print(f'O maior entre os números {n1} e {n2}, é {max(n1, n2)}')
        if op == 4:
            print('Digite os novos números')
            break
        if op == 5:
            print('Programa finalizado com sucesso.')
            exit()
