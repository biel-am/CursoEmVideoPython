days = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro percorreu? '))
pag = (km*0.15)+(days*60)
print(f'O total a pagar é de R${pag:.2f}')
