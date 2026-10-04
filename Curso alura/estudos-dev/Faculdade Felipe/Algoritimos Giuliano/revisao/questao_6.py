alunos = {}
def adicionar_aluno_e_nota():
    nome = input('nome do aluno que deseja adicionar: ')
    if nome not in alunos:
        alunos[nome] = {}
    disciplina = input('Digite o nome da disciplina: ')
    if disciplina not in alunos[nome]:
        alunos[nome][disciplina] = [] 
    quantidade_notas = int(input(f'digite a quantidade de notas da disciplina {disciplina}: '))  
    for c in range(quantidade_notas):
        notas = float(input('Digite a nota: '))
        alunos[nome][disciplina].append(notas)  

def exibir_alunos():
    print('Alunos cadastrados!')
    print('')
    for nome, nota in alunos.items():
        print(f'{nome}:{nota}')

def calcular_media():
    for nome, disciplina in alunos.items():
        print(f'Aluno: {nome}')
        for nome_disciplina, notas in disciplina.items():
            media = sum(notas)/len(notas)
            if media >= 7:
              print(f'Aprovado na disciplina: {nome_disciplina} com a nota: {media}')
            else:
               print(f'Reprovado na displicina: {nome_disciplina} com a nota : {media}')
def menu():
    print('Seja bem vindo ao sistema!')
    print(' ')
    print('Digite 1 para adicionar aluno')
    print('Digite 2 para exibir alunos')
    print('Digite 3 para calcular a media')
    print('Digite 4 para sair do sistema')   


    while True:
        função = int(input('Digite a função que quer usar: '))
        if função == 1:
            adicionar_aluno_e_nota()
        elif função == 2:
            exibir_alunos()
        elif função == 3:
            calcular_media()       
        elif função == 4:
            print('saindo...')
            break

menu()
print(alunos)