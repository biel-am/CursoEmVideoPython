from datetime import datetime
current_year = datetime.now().year
more_18 = 0
less_18 = 0
for c in range(0, 7):
    birth_year = int(input('Digite seu ano de nascimento: '))
    if current_year - birth_year >= 18:
        more_18 += 1
    else:
        less_18 += 1
print(f'Total de maiores de idade: {more_18}')
print(f'Total de menores de idade: {less_18}')
