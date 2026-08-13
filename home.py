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
            workout_page(page, user, go_home=lambda e: home_page(page, user))

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
        size=18,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E9A53F",
        text_align=TextAlign.CENTER,
    )

    leaderboard = Container(
        width=280,
        height=175,
        bgcolor="#FFFFFF",
        border_radius=18,
        border=Border.all(2, "#FFD1DC"),
        padding=10,
        content=Column(
            controls=[
                Text(
                    "🥇 Person 01",
                    size=12,
                    font_family="Fredoka",
                    color="#333333",
                ),

                Text(
                    "🥈 Person 02",
                    size=12,
                    font_family="Fredoka",
                    color="#333333",
                ),

                Text(
                    f"🥉 {user_name}",
                    size=12,
                    weight=FontWeight.BOLD,
                    font_family="Fredoka",
                    color="#E78E19",
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=7,
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

            subtitle,

            Container(height=20),

            streak_card,

            Container(height=22),

            start_workout_button,

            Container(height=25),

            leaderboard_title,

            Container(height=8),

            leaderboard,

            Container(height=15),
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

    phone.content = Stack(
        controls=[
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