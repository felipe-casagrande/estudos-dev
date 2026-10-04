empresa = {}
def adicionar_funcionario(nome,salario,cargo):
    empresa[nome] = {
        'salario':salario,
        'cargo':cargo,
    }


def consultar(nome):
   print(f'nome | cargo | salario')
   if nome in empresa:
        dados = empresa[nome]
        print(f'{nome} | {dados['salario']} | {dados['cargo']}')



def exibir():
    for nome,pessoa in empresa.items():
        print(f'{nome} | {pessoa['salario']} | {pessoa['cargo']}')    

adicionar_funcionario('felipe',200,'aa')
adicionar_funcionario('joao',200,'aa')
consultar('felipe')         
exibir()