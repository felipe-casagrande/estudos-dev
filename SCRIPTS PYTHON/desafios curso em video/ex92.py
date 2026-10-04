from datetime import datetime
dados = {}

dados['nome']= input('Digite seu nome: ')
dados['ano de nascimento'] = int(input('Digite o ano de seu  nascimento: '))
dados['carteira de trabalho'] = int(input('carteira de trabalho: '))
dados['idade'] =  datetime.now().year - dados['ano de nascimento']

if dados['carteira de trabalho'] != 0:
    dados['ano de contração'] = int(input('Digite o ano da contração: '))
    dados['salário'] = float(input('Digite seu salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano de contração']+35) - datetime.now().year) 
print('-='*30)
for k, v in dados.items():
    print(f'{k}: {v}')

        
   