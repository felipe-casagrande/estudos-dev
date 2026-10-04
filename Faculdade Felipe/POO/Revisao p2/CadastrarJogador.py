import pandas as pd
import Jogador

class CadastrarJogadores:
    def __init__(self):
        self.df = pd.DataFrame(columns=[
           'nome','sobrenome','idade','altura','tipo','arma','ataque_nome','dano_ataque'
        ])

    def cadastrar(self,jogador:'Jogador'):
        nova_linha = {
            'nome': jogador.nome,
            'sobrenome':jogador.sobrenome,
            'idade': jogador.idade,
            'altura': jogador.altura,
            'tipo': jogador.tipo,
            'arma': jogador.arma,
            'ataque_nome':jogador.ataque_nome,
            'dano_ataque':jogador.dano_ataque
        } 
        self.df = pd.concat([self.df,pd.DataFrame([nova_linha])],ignore_index=True)

    def listar(self):
        print('Jogadores cadastrados!!')
        print(self.df.to_string(index=False))