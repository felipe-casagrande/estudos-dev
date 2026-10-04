'''Uma escola precisa de um sistema para gerenciar alunos e suas notas. O sistema deve 
armazenar as informações dos alunos e permitir:
1. Adicionar um novo aluno com seu nome e uma lista de notas.
2. Adicionar uma nota a um aluno existente.
3. Calcular a média das notas de um aluno.
4. Exibir todos os alunos e suas médias.

'''
#nesse meu dicionario, as chaves sao os nomes, entao nao tem uma chave 'nome', a chave ja é o proprio nome, ex a chave ser felipe
alunos = {}
def adicionar_aluno(nome):
    alunos[nome] = []
    #exemplo
    #alunos['nome'] = 'Gioliano'


def adicionar_nota(nome,nota):
    alunos[nome].append(nota)               #dentro do meu dicionario alunos, eu crio a chave com a funçao adicionar aluno, nessa chave o valor dela vai ser muma lista vazia.
                                            # com a função adicionar nota, eu dou um append e as notas vao ser adicionadas na minha lista, que é o valor da minha chave
    # alunos['gioliano'] = 5



def calcular_media(nome):                                   #soma os valores da chave nome, que no caso sao as notas e divide com a quantidade de notas de cada aluno 
    media = sum(alunos[nome]) / len(alunos[nome])
    #print(sum(alunos[nome]))
    #print(len(alunos[nome]))
    return media



def exibir():
    for nome, nota in alunos.items():
        notas_formatadas = ','.join(map(str,nota))    #o map serve pra iterar uma lista sem usar uma estrutura de repetição para fazer um loop
        media = calcular_media(nome)
        print(f'Nome: {nome:<15} - Nota:{notas_formatadas:<5} - Média:{media:<5}')
        
      


adicionar_aluno('gioliano')
adicionar_aluno('felipe')
adicionar_nota('felipe',5)
adicionar_nota('felipe', 9)
adicionar_nota('gioliano', 5)
adicionar_nota('gioliano',7)    

nome = 'felipe'
media1 = calcular_media('felipe')


print(f'A media do {nome} é {media1}')

exibir()
