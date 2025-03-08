def cont(ini, fim, passo):
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if ini > fim and passo > 0:
        passo *= -1
    if ini > fim:
        fim -= 1
    else:
        fim += 1
    for c in range(ini, fim, passo):
        print(c, end=' ')
    print('FIM!')


print('-='*20)
print(f'Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11, 1):
    print(c, end=' ')
print('FIM!')
print('-=' * 20)
print(f'Contagem de 10 até 0 de 2 em 2')
for c in range(10, -1, -2):
    print(c, end=' ')
print('FIM!')
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 20)
cont(i, f, p)
