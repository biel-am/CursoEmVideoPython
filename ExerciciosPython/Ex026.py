frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Quantas vezes a letra "A" aparece? {frase.count('A')}')
print(f'Posição da 1ª letra "A": {frase.find('A')}')
print(f'Posição da última letra "A": {frase.find('A', -1)}')
