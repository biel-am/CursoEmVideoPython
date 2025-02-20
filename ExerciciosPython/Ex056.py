age_avg = 0
people_count = 0
older_man_name = ''
older_man_age = 0
women_less_20 = 0
for c in range(1, 5):
    name = str(input(f'Digite o nome da {c}º pessoa: ')).strip().capitalize()
    age = int(input(f'Digite a idade da {c}º pessoa: '))
    sex = str(input(f'Digite o sexo da {c}º pessoa (M/F): ')).strip().upper()
    age_avg += age
    people_count += 1
    if sex == 'M' and age > older_man_age:
        older_man_name = name
        older_man_age = age
    if sex == 'F' and age <= 19:
        women_less_20 += 1
print(f'A média de idade do grupo foi: {age_avg/people_count}.')
print(f'O nome do homem mais velho é {older_man_name} com {older_man_age}.')
print(f'Um total de {women_less_20} mulheres tem menos de 20 anos.')
