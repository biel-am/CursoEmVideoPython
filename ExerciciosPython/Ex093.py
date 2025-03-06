player = {}
goals = []
player['name'] = str(input('Nome do Jogador: ')).strip().title()
matches = int(input(f'Quantas partidas {player['name']} jogou? '))
for c in range(1, matches+1):
    goal = int(input(f'Quantos gols na partida {c}? '))
    goals.append(goal)
player['goals'] = goals
player['total'] = sum(goals)
print('-='*30)
print(player)
print('-='*30)
for k, v in player.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*30)
print(f'O jogador {player['name']} jogou {matches}.')
for p, v in enumerate(player['goals']):
    print(f'   => Na partida {p+1}, fez {v} gols.')
print(f'Foi um total de {player['total']} gols.')
