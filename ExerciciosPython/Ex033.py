n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior número é o {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é o {n2}')
else:
    print(f'O maior número é o {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor número é o {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é o {n2}')
else:
    print(f'O menor número é o {n3}')
