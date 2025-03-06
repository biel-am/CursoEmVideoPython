from datetime import datetime
current_year = datetime.now().year
person_info = {}
while True:
    person_info['name'] = str(input('Nome: ')).strip().title()
    person_info['age'] = current_year - int(input('Ano de Nascimento: '))
    if person_info['age'] < 18:
        person_info['ctps'] = 0
        break
    person_info['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    person_info['hire_year'] = int(input('Ano de Contratação: '))
    person_info['salary'] = float(input('Salário: R$'))
    person_info['retirement'] = person_info['age'] + (person_info['hire_year'] + 35) - current_year
    break
for k, v in person_info.items():
    print(f'{k} tem o valor {v}')
