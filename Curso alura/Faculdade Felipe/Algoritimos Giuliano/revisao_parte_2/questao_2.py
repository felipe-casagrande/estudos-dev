'''Um clube esportivo quer classificar seus atletas de acordo com a idade. Implemente um 
programa que receba o nome e a idade do atleta e classifique nas seguintes categorias:
• "Infantil" → até 12 anos
• "Juvenil" → 13 a 17 anos
• "Adulto" → 18 a 35 anos
• "Master" → acima de 35 anos
O sistema deve permitir o cadastro de vários atletas e exibir a lista com seus nomes, idades e 
categorias.'''
jogadores = {}

def adicionar_jogador(nome,idade):
    if idade <=12:
        jogadores[nome] = {'idade':idade,
                        'categoria':'infantil'
        }
    elif idade >=13 and idade <=17:
        jogadores[nome] = {
             'idade':idade,
             'categoria':'juvenil'
        }
    elif idade >=18 and idade <=35:
        jogadores[nome] = {
             'idade':idade,
             'categoria':'adulto'
        }
    elif idade>35:
        jogadores[nome] = {
            'idade':idade,
            'categoria':'master'
        }
        
def exibir_jogadores():
    for nome,categoria in jogadores.items():
        print(f'nome: {nome}')
        print(f'Categoria {categoria['categoria']}, idade: {categoria['idade']}')
            

def menu():
    print('digite 1 para adicionar jogadores')
    print('digite 2 para exibir os jogadores cadastrados')
    print('Digite 3 para fechar o programa.')
    while True:
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            nome = input('digite o nome do jogador: ')
            idade = int(input('Digite a idade do jogador: '))
            adicionar_jogador(nome,idade)
        elif opcao == 2:
            exibir_jogadores()
        elif opcao == 3:
            print('encerrando..')
            break
menu()

