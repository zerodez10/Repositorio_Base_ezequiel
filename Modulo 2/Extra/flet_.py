import flet as ft
def main(page: ft.Page):
    page.theme_mode ="dark"
    text = ft.Text("Login", size=30, color=  "red")
    entrega_texto= ft.TextField(width=400, color= "purple", focused_border_color="white")
    text_2 = ft.Text("Senha", size=30)
    entrega_texto_2= ft.TextField(width=400, password=True, can_reveal_password=True)
    def click(e):
        login = text.value
        print("XD", login)
    botao = ft.ElevatedButton("José é espancado", on_click=click)
    page.add(ft.Row([text,entrega_texto,]), 
            ft.Row([text_2, entrega_texto_2]),
            ft.Row([botao]))
     
ft.app(target= main)
