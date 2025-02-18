from random import randint
user_num = int(input('Digite um número inteiro de 0 a 5: '))
bot_num = randint(0, 5)
print(f'Seu número foi {user_num}')
print(f'O número da máquina foi {bot_num}')
if user_num == bot_num:
    print('Você perdeu')
else:
    print('Você venceu!')
