height = float(input('Digite sua altura (m): '))
weight = float(input('Digite seu peso (kg): '))
imc = weight/(height**2)
if imc <= 18.5:
    print('Abaixo do Peso')
if 18.5 < imc <= 25:
    print('Peso Ideal')
if 25 < imc <= 30:
    print('Sobrepeso')
if 30 < imc <= 40:
    print('Obesidade')
if 40 < imc:
    print('Obesidade Mórbida')
