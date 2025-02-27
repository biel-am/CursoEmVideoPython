print('='*30)
print(f'{"BANCO MAXQUEICOM":^30}')
print('='*30)
total_cash = int(input('Digite o valor à ser sacado: R$'))
bills_50 = total_cash // 50
total_cash -= bills_50*50
bills_20 = total_cash // 20
total_cash -= bills_20*20
bills_10 = total_cash // 10
total_cash -= bills_10*10
bills_1 = total_cash
print(f'Total de {bills_50} cédulas de R$50')
print(f'Total de {bills_20} cédulas de R$20')
print(f'Total de {bills_10} cédulas de R$10')
print(f'Total de {bills_1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO MAXQUEICOM! Tenha um bom dia!')
