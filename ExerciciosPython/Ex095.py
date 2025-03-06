players = []
goals = []
while True:
    player = {}
    print('-'*40)
    player['name'] = str(input('Nome do Jogador: ')).strip().title()
    while True:
        matches = int(input(f'Quantas partidas {player['name']} jogou? '))
        if matches < 1:
            print('Valor inválido, digite novamente.')
        else:
            break
    for c in range(1, matches+1):
        goal = int(input(f'Quantos gols na partida {c}? '))
        goals.append(goal)
    player['goals'] = goals.copy()
    player['total'] = sum(goals)
    goals.clear()
    players.append(player.copy())
    player.clear()
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if not op or op not in 'S' 'N':
            print('Opção inválida, digite novamente.')
        else:
            break
    if op == 'N':
        break
print('-='*20)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":}')
print('-'*40)
for p, pl in enumerate(players):
    print(f'{p:>3} {players[p]['name']:<15}{players[p]['goals'].__str__():<15}{players[p]['total']}')
while True:
    print('-'*40)
    while True:
        data = int(input('Mostrar dados de qual jogador (999 para parar)? '))
        if data == 999:
            break
        elif data < 0 or data > len(players)-1:
            print('Opção inválida, digite novamente.')
        else:
            break
    if data == 999:
        print('Programa encerrado com sucesso.')
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {players[data]['name']}:')
    for p, v in enumerate(players[data]['goals']):
        print(f'   => Na partida {p+1}, fez {v} gols.')
