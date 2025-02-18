distance = float(input('Digite a distância da viagem (km): '))
if distance <= 200:
    ticket = distance*0.50
else:
    ticket = distance*0.45
print(f'Viagem de {distance:.2f}km')
print(f'Valor à ser pago: R${ticket:.2f}')
