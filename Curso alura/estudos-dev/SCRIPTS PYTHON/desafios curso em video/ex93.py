jogador = dict()
gol_partida = list()
jogador['nome'] = input('Digite seu nome: ')
qnt_jogos = int(input('quantas partidas? '))
for c in range(0,qnt_jogos):
    gol_partida.append(int(input(f'quantos gols na partida {c+1}:')))
jogador['gols'] = gol_partida[:]
jogador['total'] = sum(gol_partida)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'No campo {k}, tem valor o de {v}')



for c, v in enumerate(jogador['gols']):
    print(f'Na partida {c+1}°, fez {v} gols ! ')
print(f'Foi um total de {jogador["total"]} gols em {len(jogador['gols'])} jogos!')