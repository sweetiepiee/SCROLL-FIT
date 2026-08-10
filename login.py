from flet import *
#Function that creates and displays the login page
def login_page(page):
    page.clean()

    #Sets the background colour of the page
    page.bgcolor = "#FFF4C7"

    #Creates the title banner at the top of the login page
    title = Text(
        "Welcome Back!",
        soze=32,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19"
    )

    #Creates the username input field
    username = ft.TextField(
        hint_text = "Username",
        width = 250,
        height = 45,
        border_radius = 20,
        bgcolor = "#FFFFFF",
    )

    #Creates the password input field
    password = ft.TextField(
        hint_text="Password",
        password=True,
        can_reveal_password=True,
        width=250,
        height=45,
        border_radius=20,
        bgcolor="#FFFFFF"
    )

    #Function that runs when the login button is clicked
    def login(e):

        #Checks that both username and password fields are filled in
        if username.value and password.value:
            print("Login Successful!")


    #Creates the login button
    login_button = ft.ElevatedButton(
        "LOG IN",
        on_click=login,
        bgcolor = "#A8E6A3",
        color="black",
    )

    #Creates the sign-up button
    signup_button = ft.ElevatedButton(
        "SIGN UP",
        bgcolor="#A8E6A3",
        color="black",
    )

    #Adds everything to the page
    page.add(
        Column(
            controls=[
                title,
                Container(height=40),
                username,
                password,
                Container(height=20),
                login_button,
                signup_button,
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
    )


