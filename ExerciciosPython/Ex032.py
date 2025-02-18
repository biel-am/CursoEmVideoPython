from calendar import isleap
year = int(input(f'Digite um ano: '))
if isleap(year):
    print(f'{year} é bissexto')
else:
    print(f'{year} não é bissexto')
