'''jogador = dict()
time = list()
partida = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Digite seu nome: ')
    qnt_jogos = int(input('Quantas partidas? '))

    # Usando compreensão de lista para adicionar os gols
    partida = [int(input(f'Quantos gols na partida {c+1}: ')) for c in range(qnt_jogos)]
    jogador['gols'] = partida  # Não é necessário copiar com [:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())

    # Validação de entrada simplificada
    seguir = ''
    while seguir not in 'SN':
        seguir = input('Deseja seguir? [sim/nao] ').strip().upper()[0]
    
    if seguir == 'N':
        break

# Exibição da tabela
print('-' * 50)
headers = ["COD", "Nome", "Partidas", "Total de Gols"]
print(" ".join(f'{header:<15}' for header in headers))
print('-' * 50)

for k, v in enumerate(time):
    print(f'{k:<4} {v["nome"]:<15} {len(v["gols"]):<10} {v["total"]:<15}')
print('-' * 50)

# Busca detalhada
while True:
    busca = int(input('Buscar dados de qual jogador? [999 para interromper] '))
    if busca == 999:
        break
    if not (0 <= busca < len(time)):  # Validação mais robusta
        print(f'Erro! Não existe jogador com o código {busca}')
    else:
        print(f'\nLevantamento do jogador {time[busca]["nome"]}:')
        print(f'Total de partidas: {len(time[busca]["gols"])}')
        print(f'Total de gols: {time[busca]["total"]}')
        print('Gols por partida:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  Partida {i + 1}: {g} gols')
        print('-' * 50)

print('Programa encerrado!')
'''

jogador = dict()  # Dicionário para armazenar os dados de cada jogador
time = list()  # Lista para armazenar todos os jogadores
partida = list()  # Lista para armazenar os gols por partida

# Loop para cadastrar os jogadores
while True:
    jogador.clear()  # Limpa os dados do jogador anterior
    jogador['nome'] = input('Digite seu nome: ')  # Pergunta o nome do jogador
    qnt_jogos = int(input('Quantas partidas? '))  # Pergunta a quantidade de partidas

    # Preenche os gols do jogador em cada partida
    partida = [int(input(f'Quantos gols na partida {c+1}: ')) for c in range(qnt_jogos)]
    jogador['gols'] = partida[:]  # Guarda os gols nas partidas
    jogador['total'] = sum(partida)  # Soma os gols para calcular o total
    time.append(jogador.copy())  # Adiciona o jogador à lista 'time'

    # Pergunta se deseja adicionar outro jogador **após** o cadastro completo
    seguir = input('Deseja adicionar outro jogador? [sim/nao] ').strip().upper()[0]
    
    if seguir == 'N':  # Se a resposta for 'N', encerra o loop
        break  # Encerra o loop de cadastro de jogadores

# Exibição dos dados dos jogadores cadastrados
print('-' * 50)
headers = ["COD", "Nome", "Partidas", "Total de Gols"]
print(" ".join(f'{header:<15}' for header in headers))  # Exibe o cabeçalho da tabela
print('-' * 50)

# Exibe os jogadores cadastrados com suas respectivas informações
for k, v in enumerate(time):  # Para cada jogador, exibe os dados
    print(f'{k:<4} {v["nome"]:<15} {len(v["gols"]):<10} {v["total"]:<15}')
print('-' * 50)

# Busca detalhada de um jogador específico
while True:
    busca = int(input('Buscar dados de qual jogador? [999 para interromper] '))
    if busca == 999:  # Se o código for 999, sai da busca
        break
    if not (0 <= busca < len(time)):  # Valida se o código do jogador é válido
        print(f'Erro! Não existe jogador com o código {busca}')
    else:
        # Exibe os detalhes do jogador escolhido
        print(f'\nLevantamento do jogador {time[busca]["nome"]}:')
        print(f'Total de partidas: {len(time[busca]["gols"])}')
        print(f'Total de gols: {time[busca]["total"]}')
        print('Gols por partida:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  Partida {i + 1}: {g} gols')
        print('-' * 50)

print('Programa encerrado!')
