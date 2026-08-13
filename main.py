from flet import *

from login import login_page
from home import home_page
from profile import profile_page
from workout import workout_page


# ==================================================
# MAIN FUNCTION
# ==================================================

def main(page: Page):

    # --------------------------------------------------
    # PAGE SETTINGS
    # --------------------------------------------------

    # Set the title shown for the app
    page.title = "Fit Scroll"

    # Set the background outside the phone
    page.bgcolor = "#080808"

    # Remove default page spacing
    page.padding = 0

    # Store the currently logged-in user's information
    current_user = None


    # ==================================================
    # LOGIN
    # ==================================================

    def open_login(e=None):

        # Open the login page
        # When the user successfully logs in,
        # open_home will be called
        login_page(page, open_home)


    # ==================================================
    # HOME
    # ==================================================

    def open_home(user):

        # Allow this function to change current_user
        nonlocal current_user

        # Save the logged-in user's information
        current_user = user

        # Open the home page
        # Pass the navigation functions so the
        # buttons can move between pages
        home_page(
            page,
            current_user,
            go_profile=open_profile,
            go_workout=open_workout,
        )


    # ==================================================
    # PROFILE
    # ==================================================

    def open_profile(e=None):

        # Only open the profile if a user is logged in
        if current_user:

            profile_page(
                page,
                current_user,

                # Navigation buttons
                go_home=open_home_current,
                go_workout=open_workout,

                # Logout button
                go_login=open_login,
            )


    # ==================================================
    # HOME FROM NAVIGATION
    # ==================================================

    def open_home_current(e=None):

        # Only open the home page if a user is logged in
        if current_user:

            home_page(
                page,
                current_user,

                # Navigation buttons
                go_profile=open_profile,
                go_workout=open_workout,
            )


    # ==================================================
    # WORKOUT
    # ==================================================

    def open_workout(e=None):

        # Only open the workout page if a user is logged in
        if current_user:

            workout_page(
                page,
                current_user,

                # Navigation buttons
                go_home=open_home_current,
                go_profile=open_profile,
            )


    # ==================================================
    # STARTING SCREEN
    # ==================================================

    # --------------------------------------------------
    # PHONE CONTAINER
    # --------------------------------------------------

    # Create the main phone-shaped container
    phone = Container(
        width=400,
        height=850,
        bgcolor="#FFF4C7",
        border_radius=35,
    )


    # --------------------------------------------------
    # LOGO
    # --------------------------------------------------

    # Display the Fit Scroll logo
    logo = Image(
        src="logo.png",
        width=350,
        height=400,
        fit=BoxFit.CONTAIN,
    )


    # --------------------------------------------------
    # APP TITLE
    # --------------------------------------------------

    title = Text(
        "Fit Scroll",
        size=40,
        weight=FontWeight.BOLD,
        font_family="Arial",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )


    # --------------------------------------------------
    # APP DESCRIPTION
    # --------------------------------------------------

    description = Text(
        "Move more. Scroll less.",
        size=20,
        weight=FontWeight.W_500,
        font_family="Fredoka",
        color="#E76119",
        text_align=TextAlign.CENTER,
    )


    # --------------------------------------------------
    # GET STARTED BUTTON
    # --------------------------------------------------

    # Button that takes the user to the login page
    start_button = ElevatedButton(
        "Get Started!",
        width=220,
        height=55,
        on_click=open_login,

        style=ButtonStyle(
            bgcolor="#FF7890",
            color=Colors.WHITE,
            elevation=5,
            shadow_color="#E85F78",
            shape=RoundedRectangleBorder(radius=30),

            text_style=TextStyle(
                font_family="Fredoka",
                size=20,
                weight=FontWeight.BOLD,
            ),
        ),
    )


    # --------------------------------------------------
    # FAKE PHONE CAMERA
    # --------------------------------------------------

    # Creates the black camera notch at the top
    # of the phone interface
    camera = Container(
        width=120,
        height=32,
        bgcolor="#000000",
        border_radius=20,

        # Prevents the camera notch from
        # blocking clicks
        ignore_interactions=True,
    )


    # ==================================================
    # STARTING SCREEN LAYOUT
    # ==================================================

    # Use a Stack so the camera notch can sit
    # over the main content
    phone.content = Stack(
        controls=[

            # --------------------------------------------------
            # MAIN CONTENT
            # --------------------------------------------------

            Column(
                controls=[

                    # Space above the logo
                    Container(height=80),

                    # App logo
                    logo,

                    # App name
                    title,

                    # App tagline
                    description,

                    # Space before the button
                    Container(height=40),

                    # Get Started button
                    start_button,
                ],

                # Centre everything horizontally
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),

            # --------------------------------------------------
            # CAMERA NOTCH
            # --------------------------------------------------

            Container(
                alignment=Alignment(0, -0.95),
                content=camera,

                # Prevent the notch from blocking clicks
                ignore_interactions=True,
            ),
        ],
    )


    # ==================================================
    # DISPLAY PHONE
    # ==================================================

    # Put the phone in the centre of the browser window
    page.add(
        Container(
            expand=True,
            alignment=Alignment(0, 0),
            content=phone,
        )
    )

    # Update the page so everything appears
    page.update()


# ==================================================
# WEB BROWSER
# ==================================================

if __name__ == "__main__":

    # Import Flet using the ft alias
    import flet as ft

    # Run the app in a web browser
    ft.run(
        main,
        view=ft.AppView.WEB_BROWSER,
    )