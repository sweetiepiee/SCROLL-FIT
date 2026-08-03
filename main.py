import flet as ft

def main(page: ft.Page):
    page.title = "ScrollFit"

    page.window.width = 400
    page.window.height = 944
    page.window.resizeable = False

    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.Text(
            "Welcome to ScrollFit!",
            size = 30,
            weight=ft.FontWeight.BOLD
        )
        )

ft.run(main)

def main(page: ft.page):
    page.title = "Scroll Fit"
    