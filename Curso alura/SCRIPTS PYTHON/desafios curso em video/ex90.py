alunos = dict()
alunos['nome'] = input('Digite seu nome: ')
alunos['media']= float(input('Digite sua media: '))
print(f'Nome é igual a {alunos["nome"]}')
print(f'A média é igual a: {alunos["media"]}')
if alunos['media'] <7:
    print('Situação: Reprovado')
else:
    print('Situação: Aprovado')