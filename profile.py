from flet import *


# Function that creates and displays the profile page
def profile_page(page, user, go_home=None, go_workout=None, go_login=None):

    # Clears anything currently displayed
    page.clean()

    # Background outside the phone
    page.bgcolor = "#080808"
    page.padding = 0

    # Gets the user's information
    user_name = user["full_name"]
    email = user.get("email", "Not set")
    date_of_birth = user.get("date_of_birth", "Not set")
    fitness_level = user.get("fitness_level", "Not set")
    fitness_goal = user.get("fitness_goal", "Not set")

    # --------------------------------------------------
    # PROFILE TITLE
    # --------------------------------------------------

    profile_title = Container(
        width=175,
        height=60,
        bgcolor="#FFF3A6",
        border_radius=7,
        alignment=Alignment(0, 0),
        content=Text(
            "PROFILE",
            size=25,
            weight=FontWeight.BOLD,
            font_family="Fredoka",
            color="#111111",
        ),
    )

    # --------------------------------------------------
    # PROFILE PICTURE
    # --------------------------------------------------

    profile_icon = Container(
        width=120,
        height=120,
        bgcolor="#D1D1D1",
        border_radius=100,
        alignment=Alignment(0, 0),
        content=Icon(
            Icons.PERSON,
            size=75,
            color=Colors.WHITE,
        ),
    )

    # --------------------------------------------------
    # USER NAME
    # --------------------------------------------------

    name_text = Text(
        user_name,
        size=21,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#111111",
        text_align=TextAlign.CENTER,
    )

    # --------------------------------------------------
    # LOG OUT
    # --------------------------------------------------

    def logout(e):
        if go_login:
            go_login(e)

    logout_button = TextButton(
        "Log out →",
        on_click=logout,
        style=ButtonStyle(
            color="#FF309E",
            text_style=TextStyle(
                font_family="Fredoka",
                size=17,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    # --------------------------------------------------
    # INFORMATION BARS
    # --------------------------------------------------

    email_bar = Container(
        width=315,
        height=40,
        bgcolor="#FFDFA8",
        border_radius=25,
        padding=Padding(
            left=15,
            right=10,
            top=0,
            bottom=0,
        ),
        alignment=Alignment(-1, 0),
        content=Text(
            f"Email: {email}",
            size=15,
            weight=FontWeight.BOLD,
            font_family="Fredoka",
            color="#111111",
        ),
    )

    date_of_birth_bar = Container(
        width=315,
        height=40,
        bgcolor="#FFDFA8",
        border_radius=25,
        padding=Padding(
            left=15,
            right=10,
            top=0,
            bottom=0,
        ),
        alignment=Alignment(-1, 0),
        content=Text(
            f"Date of Birth: {date_of_birth}",
            size=15,
            weight=FontWeight.BOLD,
            font_family="Fredoka",
            color="#111111",
        ),
    )

    fitness_level_bar = Container(
        width=315,
        height=40,
        bgcolor="#FFDFA8",
        border_radius=25,
        padding=Padding(
            left=15,
            right=10,
            top=0,
            bottom=0,
        ),
        alignment=Alignment(-1, 0),
        content=Text(
            f"Fitness Level: {fitness_level}",
            size=15,
            weight=FontWeight.BOLD,
            font_family="Fredoka",
            color="#111111",
        ),
    )

    fitness_goal_bar = Container(
        width=315,
        height=40,
        bgcolor="#FFDFA8",
        border_radius=25,
        padding=Padding(
            left=15,
            right=10,
            top=0,
            bottom=0,
        ),
        alignment=Alignment(-1, 0),
        content=Text(
            f"Fitness Goal: {fitness_goal}",
            size=15,
            weight=FontWeight.BOLD,
            font_family="Fredoka",
            color="#111111",
        ),
    )

    # --------------------------------------------------
    # NAVIGATION BUTTONS
    # --------------------------------------------------

    profile_button = Button(
        "PROFILE",
        width=120,
        height=45,
        on_click=lambda e: None,
        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(radius=10),
            text_style=TextStyle(
                font_family="Fredoka",
                size=15,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    home_button = Button(
        "HOME",
        width=120,
        height=45,
        on_click=go_home if go_home else lambda e: None,
        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(radius=10),
            text_style=TextStyle(
                font_family="Fredoka",
                size=15,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    workout_button = Button(
        "WORKOUT",
        width=120,
        height=45,
        on_click=go_workout if go_workout else lambda e: None,
        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(radius=10),
            text_style=TextStyle(
                font_family="Fredoka",
                size=13,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    navigation_bar = Row(
        controls=[
            profile_button,
            home_button,
            workout_button,
        ],
        alignment=MainAxisAlignment.CENTER,
        spacing=5,
    )

    # --------------------------------------------------
    # FAKE PHONE CAMERA
    # --------------------------------------------------

    camera = Container(
        width=120,
        height=32,
        bgcolor="#000000",
        border_radius=20,
        ignore_interactions=True,
    )

    # --------------------------------------------------
    # PROFILE CONTENT
    # --------------------------------------------------

    profile_content = Column(
        controls=[
            Container(height=120),
            profile_title,
            Container(height=15),
            Stack(
                controls=[
                    profile_icon,
                ],
                width=120,
                height=120,
            ),
            Container(height=2),
            name_text,
            logout_button,
            Container(height=8),
            email_bar,
            Container(height=7),
            date_of_birth_bar,
            Container(height=7),
            fitness_level_bar,
            Container(height=7),
            fitness_goal_bar,
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=0,
        scroll=ScrollMode.AUTO,
    )

    # --------------------------------------------------
    # PHONE
    # --------------------------------------------------

    phone = Container(
        width=400,
        height=850,
        bgcolor="#FFF4C7",
        border_radius=35,
    )

    phone.content = Stack(
        controls=[
            profile_content,
            Container(
                alignment=Alignment(0, 0.88),
                content=navigation_bar,
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
            alignment=Alignment(0, 0),
            content=phone,
        )
    )