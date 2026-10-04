def comprimento_maior(primeira,segunda):
    if len(primeira) > len(segunda):
        return True
    else:
        return False
    
with open('comprimento_maior.txt', 'a', encoding='utf-8') as arq:
    str1 = input('Digite uma string: ')
    str2 = input('Digite outra string: ')
    arq.write(f'A string ({str1}) é maior que a string ( {str2})? {comprimento_maior(str1,str2)}\n')
    print('Respostas salvas no arquivo txt!')

