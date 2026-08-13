from flet import *
from login import login_page
from home import home_page
from profile import profile_page
from workout import workout_page


def main(page: Page):

    page.title = "Fit Scroll"
    page.bgcolor = "#080808"
    page.padding = 0

    # Currently logged-in user
    current_user = None

    # --------------------------------------------------
    # LOGIN
    # --------------------------------------------------

    def open_login(e=None):
        login_page(page, open_home)

    # --------------------------------------------------
    # HOME
    # --------------------------------------------------

    def open_home(user):
        nonlocal current_user

        current_user = user

        home_page(
            page,
            current_user,
            go_profile=open_profile,
            go_workout=open_workout,
        )

    # --------------------------------------------------
    # PROFILE
    # --------------------------------------------------

    def open_profile(e=None):

        if current_user:

            profile_page(
                page,
                current_user,
                go_home=open_home_current,
                go_workout=open_workout,
                go_login=open_login,
            )

    # --------------------------------------------------
    # HOME FROM NAVIGATION
    # --------------------------------------------------

    def open_home_current(e=None):

        if current_user:

            home_page(
                page,
                current_user,
                go_profile=open_profile,
                go_workout=open_workout,
            )

    # --------------------------------------------------
    # WORKOUT
    # --------------------------------------------------

    def open_workout(e=None):

        if current_user:

            workout_page(
                page,
                current_user,
                go_home=open_home_current,
                go_profile=open_profile,
            )

    # --------------------------------------------------
    # STARTING SCREEN
    # --------------------------------------------------

    phone = Container(
        width=400,
        height=850,
        bgcolor="#FFF4C7",
        border_radius=35,
    )

    logo = Image(
        src="logo.png",
        width=350,
        height=400,
        fit=BoxFit.CONTAIN,
    )

    title = Text(
        "Fit Scroll",
        size=40,
        weight=FontWeight.BOLD,
        font_family="Arial",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )

    description = Text(
        "Move more. Scroll less.",
        size=20,
        weight=FontWeight.W_500,
        font_family="Fredoka",
        color="#E76119",
        text_align=TextAlign.CENTER,
    )

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

    camera = Container(
        width=120,
        height=32,
        bgcolor="#000000",
        border_radius=20,
        ignore_interactions=True,
    )

    phone.content = Stack(
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
            alignment=Alignment(0, 0),
            content=phone,
        )
    )

    page.update()


# --------------------------------------------------
# RUN APP IN WEB BROWSER
# --------------------------------------------------

if __name__ == "__main__":
    import flet as ft

    ft.run(
        main,
        view=ft.AppView.WEB_BROWSER,
    )