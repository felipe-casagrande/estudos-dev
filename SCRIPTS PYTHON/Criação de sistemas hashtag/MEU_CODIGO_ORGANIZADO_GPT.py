import flet as ft
'''
# COMANDOS
# ft.Text - Colocar um texto.
# ft.TextField - Criar uma caixa de texto, com o parâmetro label para exibir uma dica, como "Digite seu nome".
# ft.ElevatedButton - Criar um botão.
# ft.Row - Criar uma linha, onde cada item adicionado aparece lado a lado.
# ft.Column - Criar uma coluna, onde cada item adicionado aparece um abaixo do outro.
# pubsub.subscribe() - Criar um túnel de comunicação.
# pubsub.send_all() - Enviar uma mensagem para todos os conectados ao túnel.
# update() - Atualizar a interface após alterações visuais.
# .value - Obter o valor de um campo preenchido pelo usuário.
# ft.AlertDialog - Criar um pop-up/modal/alerta.
# dialog - Associar um pop-up ao parâmetro dialog da página.
# .open = True - Mostrar o pop-up na tela.
# .open = False - Fechar o pop-up.
# .add - Adicionar elementos à página.
# .remove - Remover elementos da página.
'''

def main(pagina):
    # Função para enviar mensagens no chat
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value  # Nome do usuário preenchido no pop-up
        texto_campo_enviar_mensagem = campo_enviar_mensagem.value  # Mensagem escrita pelo usuário
        mensagem = f'{nome_usuario}: {texto_campo_enviar_mensagem}'  # Formatar mensagem
        pagina.pubsub.send_all(mensagem)  # Enviar mensagem pelo túnel de comunicação
        campo_enviar_mensagem.value = ''  # Limpar o campo de entrada
        pagina.update()  # Atualizar a interface

    # Função para configurar o chat e exibir o layout do mesmo
    def entrar_no_chat(evento):
        pop_up.open = False  # Fechar o pop-up
        pagina.remove(titulo)  # Remover o título
        pagina.remove(botao)  # Remover o botão inicial
        pagina.add(chat)  # Adicionar o layout do chat
        pagina.add(linha_enviar)  # Adicionar a linha de envio de mensagens
        # Notificar que o usuário entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f'{nome_usuario} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()  # Atualizar a interface

    # Função para receber mensagens pelo túnel de comunicação
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)  # Criar um objeto de texto para exibir a mensagem
        chat.controls.append(texto)  # Adicionar a mensagem no chat
        pagina.update()  # Atualizar a interface

    # Função para exibir o pop-up
    def abrir_popup(evento):
        pagina.dialog = pop_up  # Associar o pop-up à página
        pop_up.open = True  # Abrir o pop-up
        pagina.update()  # Atualizar a interface

    # Configuração inicial da página
    titulo = ft.Text('Hashzap')  # Título inicial
    pagina.add(titulo)  # Adicionar título à página

    # Configuração do pop-up
    titulo_popup = ft.Text('Bem vindo ao hashzap')  # Título do pop-up
    caixa_nome = ft.TextField(label='Digite seu nome')  # Campo para o usuário digitar o nome
    botao_popup = ft.ElevatedButton('Iniciar chat', on_click=entrar_no_chat)  # Botão para iniciar o chat
    pop_up = ft.AlertDialog(
        title=titulo_popup,
        content=caixa_nome,
        actions=[botao_popup]
    )  # Configurar o pop-up com título, campo de texto e botão

    # Configuração do chat
    chat = ft.Column()  # Área onde as mensagens aparecerão
    campo_enviar_mensagem = ft.TextField(
        label='Digite uma mensagem',
        on_submit=enviar_mensagem
    )  # Campo de entrada para mensagens
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)  # Botão de envio
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])  # Linha com o campo e o botão de envio

    # Botão inicial da aplicação
    botao = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)
    pagina.add(botao)  # Adicionar botão inicial à página

    # Configurar o túnel de comunicação (pubsub)
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

# Iniciar a aplicação
ft.app(main, view=ft.WEB_BROWSER)
