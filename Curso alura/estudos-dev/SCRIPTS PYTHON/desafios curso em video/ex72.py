
escolha =  int(input('Digite um numero entre 0 e 20: '))
while escolha <0 or escolha >20:
    escolha = int(input('Escolha um numero valido: '))
extenso = ('zero', 'um', 'dois', 'tres',  'quatro','cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze'
           ,'catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print(f' O numero {escolha} se escreve {extenso[escolha]}')  
 
    