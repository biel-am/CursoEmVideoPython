n_user = int(input('Digite um número inteiro: '))
total = n_user
n = n_user
while True:
    if n == 1:
        break
    total *= n-1
    n = n-1
print(f'O fatorial de {n_user}, é igual a {total}')
