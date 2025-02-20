s = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print(f'A soma de todos os números pares digitados foi {s}.')
