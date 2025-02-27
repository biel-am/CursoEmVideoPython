product_count = 0
total_purchase = 0
products_over_1000 = 0
cheapest_product_name = ''
cheapest_product_price = 0
print('-='*15)
print(f'{"COMPRAS":^30}')
print('-='*15)
while True:
    while True:
        product_n = str(input('Nome do produto: ')).strip().title()
        if product_n:
            break
        elif not product_n:
            print('Nome inválido, digite novamente.')
    while True:
        product_price = int(input('Digite o preço do produto: R$'))
        if product_price > -1:
            break
        else:
            print('Preço inválido, digite novamente.')
    product_count += 1
    total_purchase += product_price
    if product_price > 1000:
        products_over_1000 += 1
    if product_count == 1:
        cheapest_product_name = product_n
        cheapest_product_price = product_price
    elif product_count != 1 and cheapest_product_price > product_price:
        cheapest_product_name = product_n
        cheapest_product_price = product_price
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if op in 'S' 'N':
            break
        elif not op or op not in 'S' 'N':
            print('Opção inválida, digite novamente.')
    if op == 'N':
        break
print('-'*30)
print(f'Total gasto: {total_purchase}')
print(f'Produtos maiores que R$1000: {products_over_1000}')
print(f'Nome do produto mais barato: {cheapest_product_name}')
