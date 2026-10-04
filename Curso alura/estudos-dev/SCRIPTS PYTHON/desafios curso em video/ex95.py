jogador = dict()
time =list()
partida = list()
while True:
    jogador.clear()
    jogador['nome'] = input('Digite seu nome: ')
    partida.clear()
    qnt_jogos = int(input('quantas partidas? '))

    for c in range(0,qnt_jogos):
        partida.append(int(input(f'quantos gols na partida {c+1}:')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        seguir = input('Deseja seguir?   [sim/nao]').upper()[0]
        if seguir in 'SN':
            break

    if seguir == 'N':
        break           
print('-'*30)
print('COD ', end='')
for j in jogador.keys():
    print(f'{j:<15}', end='')
print()    
print('-')
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()    
'''while True:
    busca = int(input('buscar dados de qual jogador?  [999 interrompe]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!, nao existe jogador com esse codigo {busca}') 
    else:
        print(f'O levamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} ele fez {g} gols!')

'''