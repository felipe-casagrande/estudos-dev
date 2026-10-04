import pandas as pd

import Jogador

class CadastroAmbiente:
    def __init__(self,nome_ambiente):
        self.nome_ambiente = nome_ambiente
        self.jogadores = []
        self.historico = pd.DataFrame(columns=[
             'rodada', 'atacante', 'defensor', 'dano_causado', 'vida_restante'
        ])

    def adicionar_jogador(self,jogador:"Jogador"):
        self.jogadores.append(jogador)
        print(f'{jogador.nome} {jogador.sobrenome} adicionado ao ambiente {self.nome_ambiente}')

    
    def listar_jogadores(self):
        print(f'Jogadores na arena {self.nome_ambiente}')
        for j in self.jogadores:
            if j.vivo:
                status = 'vivo'
            else:
                status ='morto'

            print(f'{j.nome} {j.sobrenome} {j.tipo} |Vida: {j.vida} |Status: {status} ')

print("Fim do código")
