import flet as ft

def main(page: ft.Page):
    page.title = "Olá, mundo!"
    page.scroll = "adaptive"

    # Declaração de variáveis
    nome = ft.TextField(label="Nome")

    page.add(
        ft.Text('Olá, Mundo!!!', size=50, color="red", font_family='Times new roman', weight='bold'),
        nome,
        ft.TextButton("Clique aqui")
        
        #ft.TextField(label='Digite aqui')
        #ft.Text('Meu nome é Bruno Luna, eu sou programador Python!')

    )
    page.update()

ft.app(main)