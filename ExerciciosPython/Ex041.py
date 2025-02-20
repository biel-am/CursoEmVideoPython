from datetime import datetime
birth_year = int(input('Digite seu ano de nascimento: '))
current_year = datetime.now().year
age = current_year - birth_year
print(f'Idade: {age}')
if age <= 9:
    print('Categoria: Mirim')
elif 9 < age <= 14:
    print('Categoria: Infantil')
elif 14 < age <= 19:
    print('Categoria: Junior')
elif 19 < age <= 20:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
