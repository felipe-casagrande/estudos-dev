def anagramas(s):
    if len(s) <= 1:
        return [s]
    
    anags = []
    for i, letra in enumerate(s):
        # Retira a letra i e gera anagramas das letras restantes
        restante = s[:i] + s[i+1:]
        for sub_anag in anagramas(restante):
            anags.append(letra + sub_anag)
    return anags

string = input('digite uma string e te direi os seus anagramas: ')
resultado = anagramas(string)
print(resultado)
