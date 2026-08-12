from flet import *
from signup import signup_page

#Function that creates and displays the login page
def login_page(page):
    page.clean()

    #Sets the background colour outside the phone
    page.bgcolor = "#080808"
    page.padding = 0

    #Creates the title banner at the top of the login page
    title = Text(
        "Welcome Back!",
        size=34,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
        text_align = TextAlign.CENTER,
    )

    #Creates the username input field
    username = TextField(
        hint_text = "Username",
        prefix_icon=Icons.PERSON_ROUNDED,
        width = 280,
        height = 52,
        border_radius = 25,
        bgcolor = "#FFFFFF",
        border_color = '#FFD1DC',
        focused_border_color = "#FF7890",
        text_style = TextStyle(
            font_family="Fredoka",
            size=16,
        ),
    )

    #Creates the password input field
    password = TextField(
        hint_text="Password",
        password=True,
        can_reveal_password=True,
        prefix_icon=Icons.LOCK_ROUNDED,
        width=280,
        height=52,
        border_radius=25,
        bgcolor="#FFFFFF",
        border_color = '#FFD1DC',
        focused_border_color = '#FF7890',
        text_style=TextStyle(
            font_family="Fredoka",
            size=16,
        ),
    )

    #Function that runs when the login button is clicked
    def login(e):

        #Checks that both username and password fields are filled in
        if username.value and password.value:
            print("Login Successful!")


    #Creates the login button
    login_button = ElevatedButton(
        "LOG IN",
        width= 280,
        height=55,
        on_click=login,
        style=ButtonStyle(
            bgcolor = "#FF7890",
            color=Colors.WHITE,
            elevation=3,
            shadow_color='#E85F78',
            shape=RoundedRectangleBorder(radius=28),
            text_style=TextStyle(
                font_family="Fredoka",
                size=18,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    #Creates the sign-up button
    signup_button = ElevatedButton(
        "SIGN UP",
        width= 280,
        height=55,
        on_click=lambda e: signup_page(page, lambda: login_page(page)),
        style=ButtonStyle(
            bgcolor = "#A8E6A3",
            color= "#333333",
            elevation=3,
            shape=RoundedRectangleBorder(radius=28),
            text_style=TextStyle(
                font_family="Fredoka",
                size=18,
                weight=FontWeight.BOLD,
                ),
            ),
    )

    #Creates the fake phone camera

    camera = Container(
        width=120,
        height=32,
        bgcolor='#000000',
        border_radius=20,
        ignore_interactions=True,
    )

    phone = Container(
        width=400,
        height=850,
        bgcolor='#FFF4C7',
        border_radius=35,
    )

    #Phone Content
    phone.content = Stack(
        controls=[
            #Everything inside the phone
            Column(
                controls=[
                        title,
                        Container(height=40),
                        username,
                        Container(height=8),
                        password,
                        Container(height=30),
                        login_button,
                        Container(height=25),

                        #Sign Up message
                        Text(
                            "Don't have an account?",
                            size=15,
                            font_family="Fredoka",
                            weight=FontWeight.BOLD,
                            color='#8D6E63'
                        ),
                        Container(height=8),
                        signup_button,
                        Container(height=20)
                    ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.CENTER,
                spacing=0,
                ),

                #Fake camera at the top
                Container(
                    alignment=Alignment(0,-0.95),
                    content=camera,
                    ignore_interactions=True,
                ),
        ],
    )

    #Adds everything to the page
    page.add(
        Container(
            expand=True,
            alignment=Alignment(0,0),
            content=phone,
            ),
    )
   


