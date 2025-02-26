total = 0
while True:
    n = int(input('Digite números para soma (999 para terminar): '))
    if n != 999:
        total += n
    else:
        break
print(f'A soma total dos números digitados é igual a {total}.')
