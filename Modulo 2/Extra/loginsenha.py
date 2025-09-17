import flet as ft
adic_Login = []
def lingsenha(LS: ft.Page):        
    
    def adicionar_login():
            valordologin = caixa_resposta.value
            valorsenha = caixa_resposta_2.value
            adic_Login.append(valordologin)
            adic_Login.append(valorsenha)
    def click():   
        login = caixa_resposta.value
        print(login)
    def função2(e):
          adicionar_login()
          click()
    def adicionar_login():
            valordologin = caixa_resposta.value
            valorsenha = caixa_resposta_2.value
            adic_Login.append(valordologin)
            adic_Login.append(valorsenha)
            
            if adic_Login == "isaac" and "1234":
                resultado.value= "Entrada permitida👌👍"
                resultado.color= "GREEN"
            else:
                resultado.value = "Entrada negada, vaza seu bosta"
                resultado.color = "RED"
            print(adic_Login)
            LS.update()
    def click():   
            login = caixa_resposta.value
            print(login)   
    Usuario = ft.Text("USÚARIO:", size=25)
    caixa_resposta = ft.TextField(label = "Login", width=350)
    Senha = ft.Text("SENHA:", size=25)
    caixa_resposta_2= ft.TextField(label = "Senha", width=350, password=True, can_reveal_password=True)
    botao = ft.ElevatedButton("Continuar", on_click=função2)
    resultado = ft.Text()
    LS.add(ft.Row([Usuario]), ft.Row([caixa_resposta]), ft.Row([Senha]), ft.Row([caixa_resposta_2]), ft.Row([botao]))
ft.app(target= lingsenha)
