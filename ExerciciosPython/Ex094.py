people = []
age_sum = 0
while True:
    person = {}
    person['name'] = str(input('Nome: ')).strip().title()
    while True:
        person['sex'] = str(input('Sexo [M/F]: ')).strip().upper()
        if not person['sex'] or person['sex'] not in 'M' 'F':
            print('Opção inválida, digite novamente.')
        else:
            break
    while True:
        person['age'] = int(input('Idade: '))
        if person['age'] < 0:
            print('Valor inválido, digite novamente.')
        else:
            age_sum += person['age']
            break
    people.append(person.copy())
    person.clear()
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if not op or op not in 'S' 'N':
            print('Opção inválida, digite novamente.')
        else:
            break
    if op == 'N':
        break
print('-='*20)
print(f'Total de pessoas cadastradas: {len(people)}')
print(f'Média da idade do grupo: {age_sum/len(people)}')
print(f'Lista de todas as mulheres:')
for p in people:
    if p['sex'] == 'F':
        print(p)
print(f'Lista de todas as pessoas com idade acima da média:')
for p in people:
    if p['age'] > age_sum/len(people):
        print(p)
