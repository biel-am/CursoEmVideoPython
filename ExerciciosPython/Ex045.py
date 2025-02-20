from random import choice
print('Jokenpô com máquina!')
print("""Escolha uma das opções abaixo:
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura""")
user_op = int(input('Digite a opção desejada: '))
if user_op == 1:
    user_op = 'Pedra'
if user_op == 2:
    user_op = 'Papel'
if user_op == 3:
    user_op = 'Tesoura'
bot_op = choice(('Pedra', 'Papel', 'Tesoura'))
print('Jokenpô!')
print(f'Você jogou {user_op} e a máquina jogou {bot_op}')
if user_op == bot_op:
    print('Empate')
elif (user_op == 'Pedra' and bot_op == 'Tesoura' or user_op == 'Papel' and bot_op == 'Pedra' or
        user_op == 'Tesoura' and bot_op == 'Papel'):
    print('Você venceu!')
else:
    print('Você perdeu')
