from datetime import datetime
def voto(nascimento):
    status = datetime.now().year - nascimento
    if status >= 65:
        return('Voto opcional!')
    elif status <18:
        return('Voto negado!')
    else: 
        return('Voto obrigatorio')
    
r1 = voto(int(input('Digite o seu ano de nascimento: ')))  
print(r1)
