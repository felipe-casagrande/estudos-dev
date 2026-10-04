funcionarios = {}
def adicionar_funcionario(nome,salario,cargo):
    if nome not in funcionarios:
        funcionarios[nome] = {
            'salario':salario,
            'cargo':cargo
        }
    else:
        print('Ja cadastrado')    


def consultar_funcionario(nome):
    if nome in funcionarios:
        dados = funcionarios[nome]
        print(nome)
        print(dados)
        print(f'Cargo: {dados['cargo']} | salário: R${dados['salario']:.2f}')



def exibir_funcionarios():
    print('LISTA DE FUNCIONARIOS!')
    print('')
    print(f'{'nome':<15}  {'salario':<15}{'cargo':<15}')
    for nome,dados in funcionarios.items():  
            print(f'{nome:<15}R${dados['salario']:<15}{dados['cargo']:<15}')
         
      
def menu():
    print('Digite 1 para adicionar funcionario')
    print('Digite 2 para consultar funcionario: ')
    print('Digite 3 eixbir funcionarios')
    print('Digite 4 para sair do programa')
    while True:
        opcao = int(input('Digite uma opção:' ))
        if opcao == 1:
            nome = input('Nome do funcionario: ')
            salario = float(input('Salario: '))
            cargo = input('Cargo: ')
            resultado = adicionar_funcionario(nome,salario,cargo)
        elif opcao == 2:
            nome = input('Digite o nome do funcionario que deseja consultar: ')    
            consulta = consultar_funcionario(nome)
        elif opcao == 3:
            exibir_funcionarios()
        elif opcao == 4:
            print('saindo...')
            break

menu()
print(funcionarios)       
