from random import randint
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
n_set = (n1, n2, n3, n4, n5)
print(n_set)
print(f'O maior valor é {max(n_set)}')
print(f'O menor valor é {min(n_set)}')
