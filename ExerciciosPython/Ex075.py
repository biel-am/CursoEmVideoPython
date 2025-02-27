n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))
n_set = (n1, n2, n3, n4)
pair_count = 0
print(f'Quantas vezes o número 9 aparece: {n_set.count(9)}')
if 3 in n_set:
    spot_3 = n_set.index(3)+1
else:
    spot_3 = 'Nenhum valor 3 foi digitado'
print(f'Em que posição foi digitado o primeiro valor 3: {spot_3}')
print('Números pares digitados: ', end='')
for n in n_set:
    if n % 2 == 0:
        print(n, end=' ')
