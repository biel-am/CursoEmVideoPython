numbers = []
for c in range(0, 5):
    n = int(input(f'Digite o {c}º inteiro: '))
    numbers.append(n)
print('-='*15)
print(f'Maior número digitado: {max(numbers)} - Posição ', end='')
for p, n in enumerate(numbers):
    if n == max(numbers):
        print(f'{p}', end=' ')
print('')
print(f'Menor número digitado: {min(numbers)} - Posição ', end='')
for p, n in enumerate(numbers):
    if n == min(numbers):
        print(f'{p}', end=' ')
