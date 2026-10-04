tarefas = []
def adicionar_tarefa(nome_tarefa):
    if nome_tarefa not in tarefas:
        print(f'Tarefa {nome_tarefa} foi adicionada!')
        tarefas.append(nome_tarefa)
    else:
        print('Tarefa ja cadastrada..')
       
def listar_pendentes(lista):
    print('Tarefas pendentes: ',','.join(tarefas))
   
def marcar_concluidas(lista):
    concluida = input('Qual o nome da tarefa concluida: ')
    for tarefa in lista:
        if tarefa == concluida:
            print(f'Tarefa {concluida} foi removida do sistema!')
            lista.remove(tarefa)   
         

def menu():
    print('Seja bem vindo ao sistema!')
    print(' ')
    print('Digite 1 para adicionar tarefa')
    print('Digite 2 para listar tarfeas pendentes')
    print('Digite 3 para marcar tarefas concluidas')
    print('Digite 4 para sair do sistema')   


    while True:
        função = int(input('Digite a função que quer usar: '))
        if função == 1:
            nome_tarefa = input('Qual o nome da tarefa que deseja adicionar? ')
            adicionar_tarefa(nome_tarefa) 
        elif função == 2:
            listar_pendentes(tarefas)
        elif função == 3:
            marcar_concluidas(tarefas)        
        elif função == 4:
            print('saindo...')
            break

menu()