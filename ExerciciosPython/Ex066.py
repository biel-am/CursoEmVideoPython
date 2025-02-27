count = 0
total = 0
while True:
    n = int(input('Digite um número inteiro (999 para encerrar): '))
    if n == 999:
        break
    else:
        count += 1
        total += n
print(f'A soma dos {count} números digitados é igual a {total}.')
