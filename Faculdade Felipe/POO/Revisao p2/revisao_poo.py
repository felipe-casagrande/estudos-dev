import pandas as pd
import random











j1 = Jogador('felipe','casagrande',21,1.75,'monstro','espada','rasagui',20)
j2 = Jogador('Pl','coelho',21,1.75,'monstro','espada','rasagui',20)


ambiente = CadastroAmbiente('maracana')
ambiente.adicionar_jogador(j1)
ambiente.listar_jogadores()


cad = CadastrarJogadores()
cad.cadastrar(j1)
cad.cadastrar(j2)
cad.listar()