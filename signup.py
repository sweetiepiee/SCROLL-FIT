from flet import *
#Imports the function used to save and find user accounts
from userdata import save_user, get_user

#Function that creates and displays the sign-up page
def signup_page(page, go_to_login):

    #Clears anything currently displayed on the page
    page.clean()

    #Sets the background colour outside the phone
    page.bgcolor = "#080808"
    page.padding = 0

    #SIGN UP TITLE
    
    #Creates the title at the top of the sign-up page
    title = Text(
        "Create Account",
        size=30,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )

    #INPUT FIELDS

    #Creates the full name input field
    full_name = TextField(
        hint_text="Full Name",
        prefix_icon=Icons.PERSON_ROUNDED,
        width=280,
        height=52,
        border_radius=25,
        bgcolor='#FFFFFF',
        border_color="#FFD1DC",
        focused_border_color="#FF7890",
        text_style=TextStyle(
            font_family="Fredoka",
            size=16,
        ),
    )

    #Creates the username input field
    username = TextField(
        hint_text="Username",
        prefix_icon=Icons.PERSON_ROUNDED,
        width=280,
        height=52,
        border_radius=25,
        bgcolor='#FFFFFF',
        border_color="#FFD1DC",
        focused_border_color="#FF7890",
        text_style=TextStyle(
            font_family="Fredoka",
            size=16,
        ),
    )

    #Creates the date of birth input field
    date_of_birth = TextField(
        hint_text="Date of Birth",
        prefix_icon=Icons.CALENDAR_MONTH_ROUNDED,
        width=280,
        height=52,
        border_radius=25,
        bgcolor="#FFFFFF",
        border_color="#FFD1DC",
        focused_border_color="#FF7890",
        text_style=TextStyle(
            font_family="Fredoka",
            size=16,
        ),

    )

    #Creates the email input field
    email = TextField(
        hint_text="E-mail",
        prefix_icon=Icons.EMAIL_ROUNDED,
        width=280,
        height=52,
        border_radius=25,
        bgcolor="#FFFFFF",
        border_color="#FFD1DC",
        focused_border_color="#FF7890",
        text_style=TextStyle(
            font_family="Fredoka",
            size=16,
        ),
    )

    #Creates the passwprd input field
    password = TextField(
        hint_text="Password",
        password=True,
        can_reveal_password=True,
        prefix_icon=Icons.LOCK_OUTLINE_ROUNDED,
        width=280,
        height=52,
        border_radius=25,
        bgcolor="#FFFFFF",
        border_color="#FFD1DC",
        focused_border_color="#FF7890",
        text_style=TextStyle(
            font_family="Fredoka",
            size=16,
        ),
    )

    #Creates the confirm password input field
    confirm_password = TextField(
        hint_text="Confirm Password",
        password=True,
        can_reveal_password=True,
        prefix_icon=Icons.LOCK_OUTLINE_ROUNDED,
        width=280,
        height=52,
        border_radius=25,
        bgcolor="#FFFFFF",
        border_color="#FFD1DC",
        focused_border_color="#FF7890",
        text_style=TextStyle(
            font_family="Fredoka",
            size=16,
        ),
    )

    #FITNESS LEVEL

    #Creates the fitness level dropdown
    fitness_level= Dropdown(
        hint_text="Fitness Level",
        hint_style=TextStyle(
            color='#BFC3CC',
            size=18,
        ),
        width=280,
        height=52,
        border_radius=25,
        bgcolor='#FFFFFF',
        border_color='#FFD1DC',
        focused_border_color='#FF7890',
        text_style=TextStyle(
            font_family='Fredoka',
            size=16,
            color="#BFC4CE",
        ),
        options=[
            dropdown.Option("Beginner"),
            dropdown.Option("Intermediate"),
            dropdown.Option("Advanced"),
        ],
    )

    #FITNESS GOAL
    #Creates the fitness level dropdown
    fitness_goal= Dropdown(
        hint_text="Fitness Goal",
        hint_style=TextStyle(
            color='#BFC3CC',
            size=18,
        ),
        width=280,
        height=52,
        border_radius=25,
        bgcolor="#FFFFFF",
        border_color='#FFD1DC',
        focused_border_color='#FF7890',
        text_style=TextStyle(
            font_family='Fredoka',
            size=16,
            color="#BFC4CE"
        ),
        options=[
            dropdown.Option("Lose Weight"),
            dropdown.Option("Build Up Muscle"),
            dropdown.Option("Gain Weight"),
            dropdown.Option("Stay Active"),
        ],
    )

    #SIGN UP FUNCTION

    #Function that displays a message to the user
    def show_message(message):

        #Creates a SnackBar containing the message
        page.snack_bar = SnackBar(
            content=Text(
                message,
                font_family="Fredoka",
                color=Colors.WHITE,
            ),
        )

        #Opens the SnackBar
        page.snack_bar.open = True

        #Updates the page so the message appears
        page.update()
        
    #Function that runs when sign-up button is clicked
    def signup(e):
        #Checks that all fields have been completed
        if(
            full_name.value
            and username.value
            and date_of_birth.value
            and email.value
            and password.value
            and confirm_password.value
            and fitness_level.value
            and fitness_goal.value
        ):
            #Checks whether the password and confirmation password are the same
            if password.value != confirm_password.value:

                #Displays a message in the terminal if the passwords do not match
                show_message("Passwords do not match!")

                #Stops the function from contuining
                return

            #Checks whether the username has already been registered
            if get_user(username.value):

                #Displays a message if the username already exists
                show_message("Username already exists!")

                #Stops the function from contuining
                return

            #Creates a dictionary containing all of the user's information
            user = {
                "username": username.value,
                "full_name": full_name.value,
                "date_of_birth": date_of_birth.value,
                "email": email.value,
                "password": password.value,
                "fitness_level": fitness_level.value,
                "fitness_goal": fitness_goal.value,
            }

            #Saves the new user's information to the JSON file
            save_user(user)

            #Shows a success message inside the app
            show_message("Sign Up Successful!")

            #Returns the user to the login page
            go_to_login()

        else:

            #Displays a message if one or more fields are empty
            print("Please complete all fields.")

     #SIGN UP BUTTON
     # #Creates the green sign-up button
    signup_button = ElevatedButton(
        "SIGN UP",
        width=280,
        height=55,
        on_click=signup,
        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation=3,
            shadow_color="#7FC97B",
            shape=RoundedRectangleBorder(radius=28),
            text_style=TextStyle(
                font_family="Fredoka",
                size=18,
                weight=FontWeight.BOLD,
            ),      
        ),
    )

    #Creates the log in text underneath the sign-up button
    login_text = Row(
        controls=[
            Text(
                "Already have an account?",
                size=14,
                font_family="Fredoka",
                color="#8D6E63",
                weight=FontWeight.BOLD,
            ),

            TextButton(
                "LOG IN",
                on_click=lambda  e: go_to_login(),
                style=ButtonStyle(
                    color="#FF7890",
                    text_style=TextStyle(
                        font_family="Fredoka",
                        size=14,
                        weight=FontWeight.BOLD,
                    ),
                ),
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
        spacing=3,
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

    #SCROLLABLE CONTENT 
    #Creates the column containing all sign-up information
    #This colum will be placed inside the scrollable area
    signup_content = Column(
        controls=[
            Container(height=20),
            title,
            Container(height=40),
            full_name,
            Container(height=7),
            date_of_birth,
            Container(height=7),
            email,
            Container(height=7),
            password,
            Container(height=7),
            confirm_password,
            Container(height=7),
            fitness_level,
            Container(height=8),
            fitness_goal,
            Container(height=20),
            signup_button,
            Container(height=30),
            login_text,
            Container(height=30),
        ],

        #Allows the content inside the phone to scroll
        scroll=ScrollMode.AUTO,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=0,
    )      

    #Phone Content
    phone.content = Stack(
        controls=[

            Container(
                content=signup_content,
                width=400,
                height=850,
                padding=Padding(
                    top=55,
                    left=0,
                    right=0,
                    bottom=10,
                ),
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