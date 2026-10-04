def calcularmaior(string,string2):
    return len(string) > len(string2)

string = input("Digite 1:")
string2 = input("digite a 2: ")

final = calcularmaior(string,string2)

with open("comprimentomaior.txt", 'w', encoding='utf-8') as salvar:
    salvar.write(str(final))

