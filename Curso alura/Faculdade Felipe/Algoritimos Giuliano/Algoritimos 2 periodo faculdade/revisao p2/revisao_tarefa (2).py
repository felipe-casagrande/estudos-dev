import os
import hashlib

def carregar_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = []
            for linha in arquivo:
                nome, senha = linha.strip().split(":")
                usuarios.append({"nome": nome, "senha": senha})    
        return usuarios
    except FileNotFoundError:
        return []

def salvar_usuario(nome, senha):
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome}:{senha}\n")

def cadastrar():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    if not nome or not senha:
        print('Digite algo valido..')
        return
    else:
        usuarios = carregar_usuarios()
        for usuario in usuarios:
            if usuario["nome"] == nome:
                print("Usuário já existe!")
                return
        salvar_usuario(nome, senha)
        print("Cadastro realizado!")

# Função de login
def login():
    nome = input("Nome: ")
    senha = input("Senha: ")
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            print("Login feito com sucesso!")
            return
    print("Usuário ou senha incorretos!")

def listar_usuarios():
    usuarios = carregar_usuarios()
    print("--- Usuários Cadastrados ---")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Senha: {usuario['senha']}")



def excluir_usuario(nome):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuarios.remove(usuario)
            break

    with open('usuarios.txt', 'w') as arq:
        for usuario in usuarios:
            arq.write(f"{usuario['nome']}:{usuario['senha']}\n")   
    print(f'Usuário  {nome} excluido')             

def main():
    while True:
        print("\n1 - Cadastrar\n2 - Login\n3 - Listar\n4- excluir usuario\n5 - Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
             print('Digite um unmero valido')
             continue
        if opcao == 1:
                cadastrar()
        elif opcao == 2:
                login()
        elif opcao == 3:
                listar_usuarios()
        elif opcao == 4:
                excluir = input('Digite o nome do usuario que deseja remover: ')
                excluir_usuario(excluir)
        elif opcao == 5:
            break
        

   

main()
