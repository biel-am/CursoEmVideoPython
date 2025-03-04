numbers = []
even = []
odd = []
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
numbers.append(even[:])
numbers.append(odd[:])
numbers[0].sort()
numbers[1].sort()
print(f'Valores pares: {numbers[0]}')
print(f'Valores ímpares: {numbers[1]}')
