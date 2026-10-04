alunos = {}
def adicionar_aluno_e_nota(nome,disciplina,notas):
    if nome not in alunos:
        alunos[nome] = {}
    if disciplina not in alunos[nome]:  
        alunos[nome][disciplina]= []
    alunos[nome][disciplina].extend(notas)

def exibir_alunos():
    
    for nome,disciplina in alunos.items():
        print(f'Alunos: {nome}')
        for disciplina, nota in disciplina.items():
            print(f'Disciplina: {disciplina}, nota: {nota}')

def calcular_media():
    for nome, disciplina in alunos.items():
        print(f'Aluno: {nome}')
        for nome_disciplina, notas in disciplina.items():
            media = sum(notas)/len(notas)
            if media >= 7:
                print(f'A media do {nome} na materia {nome_disciplina} é {media}, aprovado!')
            else:
                print(f'A media do {nome} na materia {nome_disciplina} é {media}: Reprovado!')    

def menu():
    print('Seja bem vindo ao sistema!')
    print('Se quiser adicionar um aluno ou uma nota do aluno no sistema, digite 1')
    print('Se quiser ver os alunos e suas notas, digite 2')
    print('Se quiser calcular medias, digite 3')
    print('Se quiser sair do sistema, digite 4')

    
    while True:
        opção = int(input('Digite o numero correspondente a açaõ que deseja: '))
        if opção == 1:
            nome = input('Nome do aluno: ')
            disciplina = input('nome da disciplina: ')
            qnt_notas = int(input('quantidade de notas: '))
            notas = []
            for c in range(qnt_notas):
                nota = float(input(f'Digite a {c+1} nota: '))
                notas.append(nota)
            adicionar_aluno_e_nota(nome,disciplina,notas)
        elif opção == 2:
            exibir_alunos()
        elif opção == 3:
            calcular_media()
        elif opção == 4:
            print('saindo do sistema')
            break    

menu()        