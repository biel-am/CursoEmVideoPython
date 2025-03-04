headquarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        headquarters[l][c] = int(input(f'Digite um valor inteiro para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {headquarters[l][c]} ]', end='')
    print('')
