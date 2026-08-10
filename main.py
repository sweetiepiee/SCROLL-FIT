from flet import *
from login import login_page

#Main function that runs the app
def main(page:Page):

    page.title = "Fit Scroll"

    #Set the background outside the phone
    page.bgcolor = "#0808085F"
    page.window.width = 460
    page.window.height = 900
    

    #Phone container
    container = Container(
        width = 400,
        height = 850,
        bgcolor = "#FFF4C7",
        border_radius=35,
        content=Column(
            controls=[],
        ),
    )

    #APP LOGO
    logo = Image(
        src = "logo.png",
        width=350,
        height=400,
        fit=BoxFit.CONTAIN,
    )

    title = Text(
        "Fit Scroll",
        size=40,
        weight=FontWeight.BOLD,
        font_family = "Fredoka",
        color = "#E78E19",
        text_align=TextAlign.CENTER,
    )
    
    description = Text(
        "Move more. Scroll less.",
        font_family="Fredoka",
        size=20,
        weight=FontWeight.W_500,
        color="#E76119",
        text_align=TextAlign.CENTER,
    )
    
    start_button = Button(
        "Get Started!",
        width = 220,
        height=55,
        style=ButtonStyle(
            text_style=TextStyle(
                font_family="Fredoka",
                size=20,
                weight=FontWeight.BOLD,
            ),
            color = Colors.WHITE,
            bgcolor = "#FF7890",
            shape = RoundedRectangleBorder(radius=30),
            elevation = 5,
            shadow_color = "#E85F78",
        ),
        on_click=lambda e: login_page(page), #Calls the function when clicked
    )

    #Fake Phone Camera
    camera = Container(
        width=120,
        height=32,
        bgcolor="#000000",
        border_radius=20,
        ignore_interactions=True,
    )
    #Add everything to the page
    container.content = Stack(
        controls=[
            Column(
                controls=[
                    Container(height=80),
                    logo,
                    title,
                    description,
                    Container(height=40),
                    start_button,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),

            Container(
                alignment=Alignment(0, -0.95),
                content=camera,
                ignore_interactions=True,
            ),
        ],

    )
    

        
    page.add(
        Container(
            expand=True,
            alignment=Alignment(0,0),
            content=container,
        )
    )

#Start the app"
run(main, assets_dir="assets")