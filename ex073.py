times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São Paulo', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Vasco', 'Grêmio', 'Criciúma', 'Fluminense', 'Vitória', 'Athletico-PR', 'Bragantino', 'Juventude', 'Corinthians', 'Cuiabá', 'Atlético-GO')
print(f'Os 5 primeiros times do campeonato são: {times[:5]}')
print('-=' * 50)
print(f'Os 4 últimos times do campeonato são: {times[-4:]}')
print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
print(f'O São Paulo está na {times.index('São Paulo') + 1}ª posição da tabela.')