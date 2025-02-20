from datetime import datetime
current_year = datetime.now().year
birth_year = int(input('Digite seu ano de nascimento: '))
age = current_year - birth_year
if age < 18:
    right_year = current_year + (18 - age)
    print(f'Seu alistamento será em {right_year}.')
elif age == 18:
    print('Seu alistamento é esse ano.')
else:
    right_year = current_year - (age - 18)
    print(f'Seu alistamento foi em {right_year}')
