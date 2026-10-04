funcionarios = []
def cadastrar_funcionario(nome,idade,cargo,salario):
    funcionario = {
        'nome':nome,
        'idade':idade,
        'cargo':cargo,
        'salario':salario,
        }
    funcionarios.append(funcionario)
    return f'Funcionario {nome} cadastrado!'
    

def exibir_funcionarios():
    if len(funcionarios) == 0:
        print('Lista de funcionarios vazia...')
    else:
        for pessoa in funcionarios:
            print(pessoa)

def insertion_sort(lista):
    tamanho = len(lista)
    for indice in range (1,tamanho):
        chave = lista[indice]
        primeiro_elemento = indice - 1
        while primeiro_elemento >=0 and lista[primeiro_elemento]['salario'] > chave['salario']:
            lista[primeiro_elemento+1] = lista[primeiro_elemento]
            primeiro_elemento -=1
        lista[primeiro_elemento+1]= chave
    return lista 


def salvar_em_arquivo():
    with open('arquivos.txt', 'w') as arq:
        for pessoa in funcionarios:
            linha = f'{pessoa['nome']};{pessoa['idade']};{pessoa['cargo']};{pessoa['salario']}\n'
            arq.write(linha)

def menu():
    print('Seja bem vindo ao sistema!')
    print('Digite 1 para cadastrar um funcionario: ')
    print('Digite 2 para exibir a lista de funcionarios ')
    print('Digite 3 para Ordenar os funcionarios por salario ')
    print('Digite 4 para salvar os dados')
    print('Digite 5 para sair do programa')
    while True:
        opcao = int(input('Digite a opção desejada: '))
        print()
        if opcao == 1:
            nome = input('Digite o nome do funcionario: ')
            try:
                idade = int(input('Digite a idade do funcionario: '))
                cargo = input('Digite o cargo: ')
                salario = float(input('Digite o valor do salário: '))
                cadastrar_funcionario(nome,idade,cargo,salario)
            except ValueError:
                print('Digite um valor valido na proxima vez...')
        elif opcao == 2:
            exibir_funcionarios()
        elif opcao == 3:
            insertion_sort(funcionarios)
            print('Funcionarios ordenado por salário: ')
            exibir_funcionarios(2)
        elif opcao == 4:
            salvar_em_arquivo()
            print('Arquivo salvo...')
        elif opcao == 5:  
            print('fechando...')
            break            
menu()
'''def carregar_em_arquivo():
    with open('arquivos.txt', 'r') as arq:
        usuarios = []
        for linha in arq:
            nome,idade,cargo,salario = linha.strip().split(';')
            usuarios.append({'nome':nome,
                             'idade':int(idade),
                             'cargo':cargo,
                             'salario':float(salario)
                             }
                             )
        return usuarios
            

cadastrar_funcionario('felipe',10,'asas',30)
cadastrar_funcionario('joao',20,'aasas',10)
cadastrar_funcionario('vitao',20,'aasas',100)

insertion_sort(funcionarios)
salvar_em_arquivo()
funcionarios = carregar_em_arquivo()
for pessoa in funcionarios:
    print(pessoa)'''