count = 0
total = 0
while True:
    n = int(input('Digite um número para coleta de informações: '))
    count += 1
    total += n
    if count == 1:
        max_num = n
        min_num = n
    else:
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n
    while True:
        op = str(input('Deseja continuar [S/N]: ')).strip().upper()
        if op == 'S':
            break
        elif op == 'N':
            print(f'A média entre todos os números foi de {total/count:.2f}')
            print(f'O maior número foi {max_num}.')
            print(f'O menor número foi {min_num}.')
            exit()
        elif not op or op not in 'S' 'N':
            print('Opção Inválida, digite novamente.')
