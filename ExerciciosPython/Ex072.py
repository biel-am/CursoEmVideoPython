n = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco',
     'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
     'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
     'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    user_n = int(input('Digite um número de 0 à 20: '))
    if user_n < 0 or user_n > 20:
        print('Número inválido, digite novamente.')
    else:
        break
print(f'Número digitado: {user_n}')
print(f'Número digitado (por extenso): {n[user_n-1]}')
