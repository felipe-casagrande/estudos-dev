notas = []
def calcular_media(nome,notas):
    media = sum(notas)/len(notas)
    print(f'media do aluno {nome} é: {media} e suas notas foram {notas}')
    if media >= 7:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')


def menu():
    print('Digite 1 para calcular media')
    print('Digite 2 para sair')
    while True:
        opcao = int(input('Digite a opçção desejada: '))
        if opcao == 1:
            nome = input('Digite o nome do aluno: ')
            qnt_notas = int(input('Digite a quantidade de notas: '))
            while qnt_notas < 5:
                print('A quantidade de notas precisa ser no minimo 5, tente novamente.')
                qnt_notas = int(input('Digite a quantidade de notas: '))
            for c in range(qnt_notas):
                nota = float(input(f'Digite sua nota {c+1}: '))
                notas.append(nota)
            calcular_media(nome,notas)
        else:
            print('Saindo..')
            break

menu()            
      