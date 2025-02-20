phrase = str(input('Digite uma frase: ')).strip().upper()
phrase = phrase.replace(' ', '')
phrase_verify = ''
for c in range(len(phrase)-1, -1, -1):
    letter = phrase[c]
    phrase_verify += letter
if phrase == phrase_verify:
    print('Essa palavra é um palíndromo.')
else:
    print('Essa palavra não é um palíndromo.')
