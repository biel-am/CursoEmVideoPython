from random import randint
total_try = 0
while True:
    user_num = int(input('Digite um número inteiro de 0 a 10: '))
    total_try += 1
    bot_num = randint(0, 10)
    print(f'Seu número foi {user_num}.')
    print(f'O número da máquina foi {bot_num}.')
    if user_num != bot_num:
        print('Você errou, tente mais uma vez.')
    else:
        break
print('Parabéns!!! Você venceu!!!')
print(f'Você acertou em {total_try} tentativas.')
