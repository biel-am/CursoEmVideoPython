first_number = int(input('Digite o primeiro termo: '))
reason = int(input('Digite a razão: '))
for c in range(first_number, first_number+(reason*10), reason):
    print(c)
