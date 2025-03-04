total_even = 0
headquarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        headquarters[l][c] = int(input(f'Digite um valor inteiro para [{l}, {c}]: '))
        if headquarters[l][c] % 2 == 0:
            total_even += headquarters[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {headquarters[l][c]} ]', end='')
    print('')
print(f'Soma dos valores pares: {total_even}')
total_3_c = headquarters[0][2] + headquarters[1][2] + headquarters[2][2]
print(f'Soma dos valores da 3º coluna: {total_3_c}')
print(f'Maior valor da segunda linha: {max(headquarters[1])}')
