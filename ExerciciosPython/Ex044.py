price = float(input('Digite o preço do produto: R$'))
print(""""Escolha uma das opções abaixo:
[ 1 ] - À vista dinheiro/cheque: 10% de desconto
[ 2 ] - À vista no cartão: 5% de desconto
[ 3 ] - Em até 2x no cartão; Preço normal
[ 4 ] - 3x ou mais no cartão: 20% de juros""")
op = int(input('Digite a opção desejada: '))
if op == 1:
    print(f'Valor total: R${price - (price*0.10):.2f}')
elif op == 2:
    print(f'Valor total: R${price - (price*0.05):.2f}')
elif op == 3:
    print(f'Valor total: R${price:.2f}')
elif op == 4:
    print(f'Valor total: R${price + (price*0.20):.2f}')
