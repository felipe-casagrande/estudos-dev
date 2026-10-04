import paineis

# Carregar e salvar dados dos usuários
def carregar_dados_usuarios():
  try:
      with open("dados.txt", 'r', encoding='utf-8') as arq:
          usuarios = []
          for linha in arq:
              nome, email, senha = linha.strip().split(":")
              usuarios.append({"nome": nome, "email": email, "senha": senha})
      return usuarios
  except FileNotFoundError:
      return []
  
def salvar_dados_usuario(nome_digitado, email_digitado, senha_digitada):
  with open('dados.txt', 'a') as arq:
     arq.write(f'{nome_digitado}:{email_digitado}:{senha_digitada}\n')

# FUNÇÕES GERAIS
def login(email_digitado, senha_digitada):
  dados_usuarios = carregar_dados_usuarios()

  for usuario in dados_usuarios:
    if usuario['email'] == email_digitado and usuario['senha'] == senha_digitada:

      email_do_usuario_logado = usuario['email']
      nome_do_usuario_logado = usuario['nome']
      email_administrador = False

      try:
        partes_do_email = email_do_usuario_logado.split('@')

        if len(partes_do_email) == 2:
          dominio = partes_do_email[1]
          if 'admin' in dominio:
            email_administrador = True
      except IndexError:
         pass
      
      if email_administrador:
          print(f'Administrador {nome_do_usuario_logado} logado com sucesso!')
          paineis.painel_admin()
          return
      else:
          print(f'Usuário {nome_do_usuario_logado} realizado com sucesso!')
          paineis.painel_usuario(email_do_usuario_logado, nome_do_usuario_logado)
      return
     
  print('Email ou senha incorretos!')

def cadastrar_usuario(nome_digitado, email_digitado, senha_digitada):
  dados_usuarios = carregar_dados_usuarios()

  for usuario in dados_usuarios:
     if usuario['email'] == email_digitado:
        print('Email já cadastrado!')
        return
  
  if len(senha_digitada) < 8 or not any(char.isdigit() for char in senha_digitada):
    print('Senha inválida. Deve ter no mínimo 8 caracteres e incluir um número.')
    return
  
  salvar_dados_usuario(nome_digitado, email_digitado, senha_digitada)
  print('Cadastro concluido com sucesso!')

# MENU INICIAL
def menu():
   while True:
      print("""
            ---- Biblioteca da paz ----
          1 - Fazer login
          2 - Fazer cadastro
          0 - Sair
            """)
      opcao = input('Escolha uma opção: ')
      if opcao == '1':
        email = input('Email: ')
        senha = input('Senha: ')
        login(email, senha)
      elif opcao == '2':
        nome = input('Digite seu nome: ')
        email = input('Digite seu melhor e-mail: ')
        senha = input('Criar senha (Mínimo 8 caracteres incluindo um número): ')
        cadastrar_usuario(nome, email, senha)
      elif opcao == '0':
         break
      else:
         print('Opção inválida!')  

if __name__ == "__main__":
    menu()