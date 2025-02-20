house_price = float(input('Digite o valor da casa: R$'))
salary = float(input('Digite o salário: R$'))
years = int(input('Digite em quantos anos quer pagar a casa: '))
installments = years * 12
installments_value = house_price / installments
if salary*0.30 >= installments_value:
    print(f'Você conseguirá fazer o empréstimo!')
    print(f'Cada parcela terá o valor de R${installments_value:.2f} no período de {installments} meses.')
else:
    print('Você não conseguirá fazer o empréstimo.')
    print('Sua parcela execeu o 30% de sua renda.')
