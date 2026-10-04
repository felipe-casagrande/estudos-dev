time = []
def adicionar_atleta(nome,idade):
    atleta = {
        'nome':nome,
        'idade':idade,
    }
    if idade <= 12:
        atleta['categoria'] = 'Infantil'
    elif idade <=17:
        atleta['categoria'] = 'Juvenil'
    elif idade <=35:
        atleta['categoria'] = 'Adulto'
    elif idade > 35:
        atleta['categoria'] = 'Master'
    time.append(atleta)


def exibir():
    print('ATLETAS CADASTRADOS!')
    print(f'{'Nome: ':<15} | {'idade':<15} | {'categoria':<15}')
    for pessoa in time:
        print(f'{pessoa['nome']:<15} | {pessoa['idade']:<15} | {pessoa['categoria']}')    


def menu():
    while True:
        opcao = int(input('Digite a opção desejada: '))    
        if opcao == 1:
            nome = input('Digite o nome do atleta: ')
            idade = int(input('Digite a idade do atleta: '))
            adicionar_atleta(nome,idade)
        elif opcao == 2:
            exibir()
        elif opcao == 3:
            print('saindo...')
            break

menu()        