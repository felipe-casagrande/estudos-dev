import index

def listar_usuarios():
    usuarios = index.carregar_dados_usuarios()
    print("\n--- Usuários Cadastrados ---\n")
    if not usuarios:
        print('Nenhum usuário cadastrado.')
        return
    for usuario in usuarios:
        seguranca_da_senha = '*' * len(usuario['senha'])
        print(f"Nome: {usuario['nome']} | Email: {usuario['email']} | Senha: {seguranca_da_senha}")