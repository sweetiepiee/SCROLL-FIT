# Home page layout
from flet import *
from profile import profile_page 
from workout import workout_page

#Function that creates and displays the home page
def home_page(page, user):

    #Clears anything currently displayed on the page
    page.clean()

    #Sets the bg colour outside the phone
    page.bgcolor = "#080808"
    page.padding = 0

    #Gets the user's name from their saved account
    user_name = user["full_name"]

    #Function that opens the profile page
    def open_profile(e):

        #Displays the profile page using logged-in user's information
        profile_page(page, user)

    #Creates the welcome message using the user's name
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

    # Creates the fire icon
    streak_icon = Text(
        "🔥",
        size=38,
    )

    # Creates the word "Streak"
    streak_title = Text(
        "Streak",
        size=15,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#333333",
        text_align=TextAlign.CENTER,
    )

    # Creates the current streak number
    streak_number = Text(
        "0 days",
        size=23,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )

    #Creates the streak card
    streak_card=Container(
        width=170,
        height=150,
        bgcolor="#FFF19A",
        border_radius=20,
        padding=10,

        #Places the streak information inside the card
        content=Column(
            controls=[
                streak_icon,
                streak_title,
                streak_number,
            ],

            #Centers the information
            horizontal_alignment=CrossAxisAlignment.CENTER,

            #Remoces automatic spacing
            spacing=0,

            #Centers the contents vertically
            alignment=MainAxisAlignment.CENTER,
        ),
    )

    #Creates the workout button
    start_workout_button = ElevatedButton(
        "START WORKOUT",
        width=300,
        height=60,

        #The workout page will be connected here later
        on_click=lambda e: workout_page(page, user),

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

    #Creates the leaderboard title
    leaderboard_title = Text(
        "LEADERBOARD",
        size=18,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E9A53F",
        text_align=TextAlign.CENTER,
    )

    #Creates the sample leaderboard
    #Temporary placeholders for now
    leaderboard = Container(
        width=280,
        height=175,
        bgcolor="#FFFFFF",
        border_radius=18,
        border=Border.all(2, "#FFD1DC"),
        padding=10,

        #Places the leaderboard users inside the card
        content=Column(
            controls=[

                #First leaderboard position
                Text(
                  "🥇 Person 01",
                  size=12,
                  font_family="Fredoka",
                  color="#333333", 
                ),

                #Second leaderboard position
                Text(
                  "🥈 Person 02",
                  size=12,
                  font_family="Fredoka",
                  color="#333333", 
                ),

                #Third leaderboard position
                Text(
                    f"🥉{user_name}",
                    size=12,
                    weight=FontWeight.BOLD,
                    font_family="Fredoka",
                    color="#E78E19",
                ),
            ],

            #Centers the leaderboard
            horizontal_alignment=CrossAxisAlignment.CENTER,

            #Adds sapcing between leaderboard positions
            spacing=7,
        ),
    )

    #Creates the PROFILE navigation button
    profile_button = ElevatedButton(
        "PROFILE",
        width=120,
        height=45,

        #Opens the user's profile when clicked
        on_click=open_profile,

        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            shape=RoundedRectangleBorder(radius=10),

            text_style=TextStyle(
                font_family="Fredoka",
                size=15,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    #Creates the HOME navigation button
    home_button = ElevatedButton(
        "HOME",
        width=120,
        height=45,

        #The user is already on the home page
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

    #Creates the CHALLENGE navigation button
    workout_button = ElevatedButton(
        "WORKOUT",
        width=120,
        height=45,

        #Will be connected later
        on_click=lambda e: workout_page(page, user, lambda: home_page(page, user)),

        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation = 2,
            shape=RoundedRectangleBorder(radius=10),

            text_style=TextStyle(
                font_family="Fredoka",
                size=15,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    #Puts the three navigation buttons next to each other
    navigation_bar = Row(
        controls=[
            profile_button,
            home_button,
            workout_button,
        ],

        alignment=MainAxisAlignment.CENTER,
        spacing=5,
    )
    #Fake Phone Camera
    camera = Container(
        width=120,
        height=32,
        bgcolor="#000000",
        border_radius=20,
        ignore_interactions=True,
    )

    #Creates the main home page content
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

        #Centers all content horizontally
        horizontal_alignment=CrossAxisAlignment.CENTER,

        #Removes automatic spacing
        spacing=0,
    )

    #Creates the phone container

    #Phone container
    phone = Container(
        width = 400,
        height = 850,
        bgcolor = "#FFF4C7",
        border_radius=35,
    )

    #Places the home content and camera inside the phone
    phone.content = Stack(
        controls=[
            home_content,
            Container(
                alignment=Alignment(0,0.88),
                content=navigation_bar,
            ),
            
            Container(
                alignment=Alignment(0, -0.95),
                content=camera,
                ignore_interactions=True,
            ),
        ],
    )

    #Adds the phone to the page
    page.add(
        Container(
            expand=True,
            alignment=Alignment(0,0),
            content=phone,
        )
    )