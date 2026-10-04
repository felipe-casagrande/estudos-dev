dados = {}
soma_idade = media = 0
lista = list()

while True:
    dados.clear()
    dados['nome'] = input('Digite seu nome: ')
    while True:
        dados['sexo'] = input('Digite seu sexo: ').upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro, por favor, digite novamente')
    dados['idade'] = int(input('Digite sua idade: '))
    soma_idade += dados['idade']

    lista.append(dados.copy())

    while True:
            seguir = input('Deseja continuar  [sim/ nao]').upper()[0]
            if seguir in 'SN':
                 break
            print('Erro, digite novamente: ')
    if seguir == 'N':
         break           
media = soma_idade / len(dados)
print('-='*30)
print(f'A) A quantidade de pessoas cadastradas foram {len(dados)}')
print(f'B) A média de idade é : {media:.2f}')
print('C) As mulheres cadasatradas foram: ', end='')
for p in lista:
      if p['sexo'] == 'F':
           print(f'{p['nome']} ', end='') 
print()              
print(f'D) As pessoas com a idade acima da media foram: ')
for p in lista:
     if p['idade'] >= media:
        print('         ', end='')
        for k, v in p.items():
             print(f'{k} : {v} ', end=' ')
        print()