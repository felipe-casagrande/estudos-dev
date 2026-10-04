import flet as ft
'''                                                             COMANDOS


# ft.Text - Colocar um texto
# ft.TextField - Criar uma caixa de texto, colocar o parametro label quando quiser colocar um texto dentro, e depois ainda fica arrumado. Tipo um 'digite seu nome'
# ft.ElevatedButton - Criar um botao
#ft.Row - criar uma linha, em que cada item que adicionar a ela, vai entrar do lado, no caso da coluna entra embaixo
ft.Columns - cria uma coluna, em que cada item q eu adiciono vai ficando um embaixo do outro, para o chat ficar como coluna.
pubsub.subscribe() - criar um tunel de comunição
pubsub.send_all ()- enviar uma mensagem para todos os que estao no tunel de comunicação
update() - sempre que for ter uma atualização visual, colocar ou tirar uma botao ou etc, dar o update pra essa atualização acontecer.
.value() - mostrar os valores da variavel que foi preenchida pelo usuario, exemplo o nome
ft.AlertDialog -  Criar um pop up/modal/alerta
dialog - Para associar a qual pop up sera executado os open
.open = True - Mostrar o pop up na tela
.open = False - Tirar o pop up da tela
.add - Adicionar algo na tela, na pagina 
.remove - Tirar algo que estava na tela
 paramentros do pop_up = 
    title= o titulo, entao antes cria uma variavel com um ft.Text e depois jogue ela no parametro tittle do AlertDialog
    content=  A caixa onde vc preenche algo, tipo aquelas de email, entao antes vc cria uma variavel com  ft.TextField e depois jogue ela no parametro quando criar o AlertDialog
    actions= Botao do pop up, criei uma variavel com o ft.ElevatedButtom
      e depois jogue ela no parametro quando criar o AlertDialog. Mas tem q passar em lista, exemplo = actions=[botao_popup]
ft.app(main) - executa a função principal sempre que o usario entra no site      
    view = WEB_BROWSER - para ser executado em sites.
'''
def main(pagina):
    # titulo
    titulo = ft.Text('Hashzap')
    pagina.add(titulo)
    
        # criar popup
        # parametros para o pop_up
    
    titulo_popup = ft.Text('Bem vindo ao hashzap')
    caixa_nome = ft.TextField(label= 'digite seu nome')
    
                 
    
    def enviar_mensagem(evento):
        
        nome_usuario = caixa_nome.value
        texto_campo_enviar_mensagem = campo_enviar_mensagem.value
        mensagem = (f'{nome_usuario}: {texto_campo_enviar_mensagem}')
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ''
        pagina.update()

    
    campo_enviar_mensagem = ft.TextField(label='digite uma mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem,botao_enviar])
    chat = ft.Column()

    
    def entrar_no_chat(evento):
        # fechar o popup        
        pop_up.open = False
        # tirar o titulo     
        pagina.remove(titulo)
        # sumir com o botao iniciar chat
        pagina.remove(botao)
        
        # carregar o chat
        pagina.add(chat)

        # carregar linha enviar mensagem
        pagina.add(linha_enviar)
        # adicionar no chat 'Fulano entrou no chat'
        nome_usuario = caixa_nome.value
        mensagem =(f'{nome_usuario} entrou no chat')
        pagina.pubsub.send_all(mensagem)
        pagina.update()
       
                              #primeiro criar a função do tunel de comunicação, depois criar o tunel, depois trocar nos lugares onde ele mandava mensagem pro proprio chat para ele mandar no tunel.
    
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)



    botao_popup = ft.ElevatedButton('iniciar chat', on_click=entrar_no_chat)      # primeiro cria a função e depois chama ela dentro do paramentro do botao.


    #colocando os paremetros na função alerta, que é o pop_up, para aparecer o titulo, parametro titlle, content para a caixa de texto, actions para os botoes, lembrando que o botao tem q passar em lista            
    
    pop_up = ft.AlertDialog(title= titulo_popup, content= caixa_nome,actions=[botao_popup])
    


    #botao inicar
    def abrir_popup(evento):
        pagina.dialog = pop_up
        pop_up.open = True
        pagina.update()
    
        

    botao = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)
    pagina.add(botao)
    
ft.app(main, view=ft.WEB_BROWSER)





'''
ORDEM DE CRIAÇÃO PARA ENTENDIMENTOS
1. Elementos e funções principais são definidos primeiro
Título e botão principal:

Você começa criando o titulo (ft.Text) e o botão principal (botao) que, inicialmente, aparecem na página.
Esses elementos são adicionados imediatamente à página:

pagina.add(titulo)
pagina.add(botao)
Função de abrir o pop-up:

A lógica para exibir o pop-up (diálogo) é criada antes mesmo de o pop-up ser definido:

def abrir_popup(evento):
    pagina.dialog = pop_up
    pop_up.open = True
    pagina.update()
2. O pop-up é configurado
O pop_up é definido usando ft.AlertDialog, incluindo título, caixa de texto e um botão de "Iniciar Chat":

pop_up = ft.AlertDialog(
    title=titulo_popup,
    content=caixa_nome,
    actions=[botao_popup]
)
O botão de ação no pop-up (botao_popup) já está associado à função que controla a entrada no chat (entrar_no_chat).
3. Funções para manipular o chat são criadas
Antes que o usuário possa interagir com o chat, a lógica do envio de mensagens e a manipulação do layout são definidas:

Função para enviar mensagens:

def enviar_mensagem(evento):
    texto = ft.Text(campo_enviar_mensagem.value)
    chat.controls.append(texto)
    pagina.update()
Função para entrar no chat:

def entrar_no_chat(evento):
    pop_up.open = False
    pagina.remove(titulo)
    pagina.remove(botao)
    pagina.add(chat)
    pagina.add(linha_enviar)
    pagina.update()

4. Elementos do chat são definidos

Os elementos que compõem o chat são configurados após as funções:
Um Column (chat) para armazenar as mensagens.
Uma Row (linha_enviar) que contém a caixa de entrada e o botão de envio:
linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

5. Interação começa com o botão principal
A execução do aplicativo começa com o botão principal "Iniciar chat".
Quando clicado, chama abrir_popup, que exibe o diálogo.
Dentro do diálogo, o botão "Iniciar Chat" chama a função entrar_no_chat, que configura e exibe o layout do chat.
Fluxo de execução em tempo de execução
A página é inicializada com:

O título (titulo).
O botão principal (botao).
Usuário clica no botão principal:

Isso chama abrir_popup, exibindo o pop-up.
Usuário interage com o pop-up:

Digita o nome e clica no botão "Iniciar Chat".
Isso chama entrar_no_chat, removendo o título e o botão principal, e exibindo o chat.
No chat, o usuário envia mensagens:

Cada mensagem é adicionada ao Column (chat.controls), que é atualizado dinamicamente.
'''