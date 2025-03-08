def area(lar, com):
    a = lar*com
    print(f'A área de um terreno {lar}*{com} é de {a:.1f}².')


print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(lar=l, com=c)
