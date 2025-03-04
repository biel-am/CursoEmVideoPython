person = []
people = []
total_people = 0
heaviest_name = []
lightest_name = []
heaviest_weight = lightest_weight = 0
counter = 0
while True:
    name = str(input('Digite o nome da pessoa: ')).strip().title()
    weight = float((input('Digite o peso da pessoa: ')))
    person.append(name)
    person.append(weight)
    people.append(person[:])
    total_people += 1
    person.clear()
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if not op or op not in 'S' 'N':
            print('Opção inválida, digite novamente.')
        else:
            break
    if op == 'N':
        break
print(f'Total de pessoas cadastradas: {total_people}')
for p in people:
    counter += 1
    if counter == 1:
        heaviest_name.append(p[0])
        heaviest_weight = p[1]
        lightest_name.append(p[0])
        lightest_weight = p[1]
    else:
        if p[1] > heaviest_weight:
            heaviest_name.clear()
            heaviest_name.append(p[0])
            heaviest_weight = p[1]
        elif p[1] == heaviest_weight:
            heaviest_name.append(p[0])
        if p[1] < lightest_weight:
            lightest_name.clear()
            lightest_name.append(p[0])
            lightest_weight = p[1]
        elif p[1] == lightest_weight:
            lightest_name.append(p[0])
print(f'O maior peso foi de {heaviest_weight:.2f}kg. Peso de {heaviest_name}')
print(f'O menor peso foi de {lightest_weight:.2f}kg. Peso de {lightest_name}')
