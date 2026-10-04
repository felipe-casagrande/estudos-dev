from random import randint
from operator import itemgetter
jogadores = {'Jogador 1': randint(1,6), 
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6)
             }
ranking = list()
for k, v in jogadores.items():
    print(f'O jogador {k}, tirou {v}')
ranking = sorted(jogadores.items(), key= itemgetter(1), reverse= True)
print('-='*30)
for c, v in enumerate(ranking):
    print(f'O {c+1} lugar foi {v[0]} com {v[1]}')

