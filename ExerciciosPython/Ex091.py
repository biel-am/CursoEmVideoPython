from random import randint
from time import sleep
from operator import itemgetter
players = {'player1': randint(1, 6),
           'player2': randint(1, 6),
           'player3': randint(1, 6),
           'player4': randint(1, 6)}
ranking = {}
counter = 1
print('Valores sorteados:')
for k, v in players.items():
    print(f'O {k} tirou {v}')
    sleep(0.8)
print('-='*20)
print('Ranking dos jogadores:')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for k, v in ranking:
    print(f'{counter}º colocado: {k} com {v}')
    counter += 1
