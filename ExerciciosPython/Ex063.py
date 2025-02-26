print('-'*30)
print('Sequência de Fibonacci')
term_count = int(input('Digite quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
count = 0
while True:
    if count == term_count:
        break
    if count == term_count-1:
        print(f'{t1}', end='')
    else:
        print(f'{t1}', end=' -> ')
    t2 += t1
    t1 = t2 - t1
    count += 1
