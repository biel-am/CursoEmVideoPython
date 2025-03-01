exp = str(input('Digite uma expressão matemática: ')).strip()
if exp.count('(') == exp.count(')'):
    print('A expressão é VÁLIDA')
else:
    print('A expressão é INVÁLIDA')
