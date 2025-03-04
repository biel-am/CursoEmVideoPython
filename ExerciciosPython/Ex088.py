from random import randint
from time import sleep
bet = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
bet_count = int(input('Quantos jogos você uqer que eu sorteie? '))
print('-=-=-= SORTEANDO 4 JOGOS -=-=-=')
for c in range(1, bet_count+1):
    while len(bet) < 6:
        n = randint(0, 60)
        if n not in bet:
            bet.append(n)
    bet.sort()
    sleep(1)
    print(f'Jogo {c}: {bet}')
    bet.clear()
sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
