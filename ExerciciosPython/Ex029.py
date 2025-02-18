speed = float(input('Digite a velocidade do carro (km/h): '))
if speed > 80:
    penalty = (speed-80)*7
    print('Você excedeu o limite de 80km/h!')
    print(f'Sua multa é de R${penalty:.2f}')
else:
    print('Você não foi multado!')
