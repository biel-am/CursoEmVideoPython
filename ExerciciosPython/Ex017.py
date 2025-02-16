from math import sqrt
cat_o = int(input('Digite o comprimento do cateto oposto: '))
cat_a = int(input('Digite o comprimento do cateto adjacente: '))
hip = sqrt((cat_o**2)+(cat_a**2))
print(f'O comprimento da hipotenusa é igual a {hip:.2f}')
