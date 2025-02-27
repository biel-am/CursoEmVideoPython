plus_18 = 0
men = 0
women_less_20 = 0
print('-='*15)
print(f'{"CADASTRO GERAL":^30}')
print('-='*15)
while True:
    while True:
        age = int(input('Digite a idade da pessoa: '))
        if age > -1:
            break
        else:
            print('Idade inválida, digite novamente.')
    while True:
        s = str(input('Digite o sexo [M/F]: ')).strip().upper()
        if s in 'M' 'F':
            break
        elif not s or s not in 'M' 'F':
            print('Opção inválida, digite novamente.')
    if age >= 18:
        plus_18 += 1
    if s == 'M':
        men += 1
    if s == 'F' and age < 20:
        women_less_20 += 1
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if op in 'S' 'N':
            break
        elif not op or op not in 'S' 'N':
            print('Opção inválida, digite novamente.')
    if op == 'N':
        break
print('-'*30)
print(f'Maior de 18 anos: {plus_18}')
print(f'Homens: {men}')
print(f'Mulheres com menos de 20 anos: {women_less_20}')
