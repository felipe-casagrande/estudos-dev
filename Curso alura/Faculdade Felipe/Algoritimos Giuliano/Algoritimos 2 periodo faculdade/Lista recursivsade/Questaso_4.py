def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return eh_palindromo(s[1:-1])
palavra = input('Digite uma palavra e te direi se é um palindromo: ')
resultado=  eh_palindromo(palavra)
print(resultado)