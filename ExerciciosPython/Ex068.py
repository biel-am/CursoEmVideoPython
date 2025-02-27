from random import randint
print('-='*15)
print(f'{"JOGO DO PAR OU ÍMPAR":^30}')
print('-='*15)
win_count = 0
while True:
    while True:
        user_num = int(input('Digite um valor (1 - 10): '))
        if 0 < user_num < 11:
            break
        else:
            print('Opção inválida, digite novamente.')
    while True:
        user_PI = str(input('Par ou Ímpar [P/I]? ')).strip().upper()
        if user_PI in 'P' 'I':
            break
        elif not user_PI or user_PI not in 'P' 'I':
            print('Opção inválida, digite novamente.')
    print('-'*30)
    bot_num = randint(1, 10)
    total_user_bot = user_num + bot_num
    if total_user_bot % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print(f'Você jogou {user_num} e o computador {bot_num}. Total de {total_user_bot} deu {result}.')
    print('-'*30)
    if total_user_bot % 2 == 0 and user_PI == 'P' or total_user_bot % 2 != 0 and user_PI == 'I':
        print('Você VENCEU!')
        win_count += 1
        print('Vamos jogar novamente...')
        print('-='*15)
    else:
        print('Você PERDEU.')
        print('-=' * 15)
        break
print(f'GAME OVER! Você venceu {win_count} vezes.')
