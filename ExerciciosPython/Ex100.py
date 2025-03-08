from random import randint
def somaPar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {num}, temos {soma}')


numbers = []
print('Sorteando os 5 valores da lista: ', end='')
for c in range(0, 5):
    random_n = randint(1, 10)
    numbers.append(random_n)
    print(random_n, end=' ')
print('PRONTO!')
somaPar(numbers)
