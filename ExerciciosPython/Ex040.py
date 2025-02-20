n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
avg = (n1+n2)/2
print(f'Sua média foi {avg}')
if avg < 5:
    print('Você foi reprovado.')
elif 5 < avg <= 6.9:
    print('Você está de recuperação.')
if avg >= 7:
    print('Você foi aprovado.')
