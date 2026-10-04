tarefas = []
def adicionar_tarefa(nome_tarefa):
    if nome_tarefa not in tarefas:
        tarefas.append(nome_tarefa)
        print(f'Tarefa {nome_tarefa} adicionada!')
    else:
        print('Tarefa ja cadastrada')

def exibir_tarefas():
    print('Tarefas Pendendes')
    print('')
    print(','.join(tarefas))

def marcar_concluida(nome):
    if nome in tarefas:
        tarefas.remove(nome)


def menu():
    print('Digite 1 para adicionar tarefa')
    print('Digite 2 para exibir tarefas')
    print('Digite 3 para marcar tarefas concluidas')
    while True:
        opcao = int(input('escolha uma opçao: '))
        if opcao == 1:
            nome_tarefa = input('Digite o nome da tarefa: ')
            adicionar_tarefa(nome_tarefa)
        elif opcao == 2:
            exibir_tarefas()
        elif opcao == 3:
            nome_tarefa = input('Digite o nome da tarefa concluida: ')
            marcar_concluida(nome_tarefa)
        elif opcao == 4:
            print('saindo...')
            break
menu()