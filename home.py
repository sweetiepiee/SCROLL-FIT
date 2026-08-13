from flet import *
from profile import profile_page
from workout import workout_page


# Function that creates and displays the home page
def home_page(page, user, go_profile=None, go_workout=None):

    # Clears anything currently displayed
    page.clean()

    # Sets the background colour outside the phone
    page.bgcolor = "#080808"
    page.padding = 0

    # Gets the user's name from their saved account
    user_name = user["full_name"]

    # --------------------------------------------------
    # PROFILE
    # --------------------------------------------------

    def open_profile(e):
        if go_profile:
            go_profile(e)
        else:
            profile_page(page, user)

    # --------------------------------------------------
    # WORKOUT
    # --------------------------------------------------

    def open_workout(e):
        if go_workout:
            go_workout(e)
        else:
            workout_page(
                page,
                user,
                go_home=lambda e: home_page(page, user)
            )

    # --------------------------------------------------
    # WELCOME
    # --------------------------------------------------

    welcome_text = Text(
        f"Hi, {user_name}!",
        size=27,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )

    subtitle = Text(
        "Let's check your activity!",
        size=15,
        font_family="Fredoka",
        color="#8D6E63",
        weight=FontWeight.BOLD,
        text_align=TextAlign.CENTER,
    )

    # --------------------------------------------------
    # STREAK CARD
    # --------------------------------------------------

    streak_icon = Text(
        "🔥",
        size=38,
    )

    streak_title = Text(
        "Streak",
        size=15,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#333333",
        text_align=TextAlign.CENTER,
    )

    streak_number = Text(
        "0 days",
        size=23,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )

    streak_card = Container(
        width=170,
        height=150,
        bgcolor="#FFF19A",
        border_radius=20,
        padding=10,
        content=Column(
            controls=[
                streak_icon,
                streak_title,
                streak_number,
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0,
            alignment=MainAxisAlignment.CENTER,
        ),
    )

    # --------------------------------------------------
    # START WORKOUT BUTTON
    # --------------------------------------------------

    start_workout_button = ElevatedButton(
        "START WORKOUT",
        width=300,
        height=60,
        on_click=open_workout,
        style=ButtonStyle(
            bgcolor="#FF7890",
            color=Colors.WHITE,
            elevation=3,
            shadow_color="#E85F78",
            shape=RoundedRectangleBorder(radius=28),
            text_style=TextStyle(
                font_family="Fredoka",
                size=25,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    # --------------------------------------------------
    # LEADERBOARD
    # --------------------------------------------------

    leaderboard_title = Text(
        "LEADERBOARD",
        size=21,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E9A53F",
        text_align=TextAlign.CENTER,
    )

    # 1st place
    first_place = Row(
        controls=[
            Text(
                "🥇",
                size=18,
            ),

            Text(
                "Person 01",
                size=14,
                font_family="Fredoka",
                weight=FontWeight.BOLD,
                color="#333333",
                expand=True,
            ),

            Text(
                "120 pts",
                size=13,
                font_family="Fredoka",
                color="#8D6E63",
            ),
        ],
        spacing=8,
    )

    # 2nd place
    second_place = Row(
        controls=[
            Text(
                "🥈",
                size=18,
            ),

            Text(
                "Person 02",
                size=14,
                font_family="Fredoka",
                weight=FontWeight.BOLD,
                color="#333333",
                expand=True,
            ),

            Text(
                "95 pts",
                size=13,
                font_family="Fredoka",
                color="#8D6E63",
            ),
        ],
        spacing=8,
    )

    # 3rd place - current user
    third_place = Row(
        controls=[
            Text(
                "🥉",
                size=18,
            ),

            Text(
                user_name,
                size=14,
                font_family="Fredoka",
                weight=FontWeight.BOLD,
                color="#E78E19",
                expand=True,
            ),

            Text(
                "80 pts",
                size=13,
                font_family="Fredoka",
                weight=FontWeight.BOLD,
                color="#E78E19",
            ),
        ],
        spacing=8,
    )

    leaderboard = Container(
        width=300,
        height=150,
        bgcolor="#FFFFFF",
        border_radius=20,
        border=Border.all(
            2,
            "#FFD1DC",
        ),
        padding=15,

        content=Column(
            controls=[
                first_place,

                Divider(
                    height=1,
                    color="#FFD1DC",
                ),

                second_place,

                Divider(
                    height=1,
                    color="#FFD1DC",
                ),

                third_place,
            ],
            spacing=6,
        ),
    )

    # --------------------------------------------------
    # NAVIGATION BUTTONS
    # --------------------------------------------------

    profile_button = ElevatedButton(
        "PROFILE",
        width=120,
        height=45,
        on_click=open_profile,
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

    home_button = ElevatedButton(
        "HOME",
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

    workout_button = ElevatedButton(
        "WORKOUT",
        width=120,
        height=45,
        on_click=open_workout,
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
    # HOME CONTENT
    # --------------------------------------------------

    home_content = Column(
        controls=[
            Container(height=65),

            welcome_text,

            Container(height=2),

            subtitle,

            Container(height=20),

            streak_card,

            Container(height=22),

            start_workout_button,

            Container(height=25),

            leaderboard_title,

            Container(height=8),

            leaderboard,
        ],

        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=0,
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

    # --------------------------------------------------
    # PHONE CONTENT
    # --------------------------------------------------

    phone.content = Stack(
        controls=[

            # Main home content
            home_content,

            # Bottom navigation
            Container(
                alignment=Alignment(0, 0.88),
                content=navigation_bar,
            ),

            # Fake camera at top
            Container(
                alignment=Alignment(0, -0.95),
                content=camera,
                ignore_interactions=True,
            ),
        ],
    )

    # --------------------------------------------------
    # ADD PHONE TO PAGE
    # --------------------------------------------------

    page.add(
        Container(
            expand=True,
            alignment=Alignment(0, 0),
            content=phone,
        )
    )

    page.update()