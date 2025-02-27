teams = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama',
         'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
         'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print(f'5 primeiros colocados do campeonato: {teams[:5]}')
print(f'4 últimos colocados do campeonato: {teams[-4:]}')
print(f'Times em ordem alfabética: {sorted(teams)}')
print(f'Posição do Grêmio: {teams.index('Grêmio')+1}º')
