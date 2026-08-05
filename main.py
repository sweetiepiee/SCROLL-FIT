import flet as ft

#Main function that runs the app
def main(page: ft.Page):

    page.title = "ScrollFit"

    #Android screen size
    page.window.width = 380
    page.window.height = 850
    page.window.resizeable = False

    #Set the background color
    page.bgcolor = "#FFFFFF"

    def start_clicked(e):
        page.clean()

        #Display a welcome message
        page.add(
            ft.Text('Welcome to ScrollFit!',
                    size=30,
                    weight=ft.FontWeight.BOLD
                    )
        )

    #APP LOGO
    logo = ft.Image(
        src = "assests/logo.png",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )

    title = ft.Text(
        "ScrollFit",
        size=40,
        weight=ft.FontWeight.BOLD,
        color = "#DB891D",
    )

    description = ft.Text(
        "Move more. Scroll less.",
        width=220,
        height=55,
        on_click=start_clicked,
    )

    start_button = ft.ElevatedButton(
        text="Get Started!",
        width = 220,
        height=55,
        on_click=start_clicked, #Calls the function when clicked
    )
    #Add everything to the page
    page.add(
        ft.Column(
            [logo,
             title,
             description,
             ft.Container(height=40),
             start_button,
             ],
             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
             alignment=ft.MainAxisAlignment.CENTER,
             expand=True,
            )

    )

#Start the app
ft.run(main)
    