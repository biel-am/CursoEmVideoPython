n_count = 0
first_number = int(input('Digite o primeiro termo: '))
total = first_number
reason = int(input('Digite a razão: '))
print('Seus 10 primeiros termos:')
while True:
    if n_count == 10:
        break
    print(total)
    total += reason
    n_count += 1
while True:
    op = int(input('Quantos termos à mais você deseja (0 para encerrar programa)? '))
    if op == 0:
        print('Programa encerrado com sucesso.')
        exit()
    n_count_limit = n_count
    while True:
        if n_count == n_count_limit+op:
            break
        total += reason
        print(total)
        n_count += 1
