palavras = 'trabalhar','aprender', 'escola', 'lara','estadio','futebol', 'inglaterra','Espanha'
for p in palavras:
    print(f'\nNa palavra {p}, temos: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
        
            