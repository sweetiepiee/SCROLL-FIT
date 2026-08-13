from flet import *

#Function that creates and displays the profile page
def profile_page(page, user):

    #Clears anything currently displayed on the page
    page.clean()

    #Sets the background color outside the page
    page.bgcolor = "#080808"
    page.padding = 0

    #Gets the user's name from their saved account
    user_name = user["full_name"]

    #Temporary test message
    profile_text = Text(
        f"Welcome to your profile, {user_name}!",
        size=24,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
    )

    #Adds the profile information to the page
    page.add(
        Container(
            width=400,
            height=850,
            bgcolor="#FFF4C7",
            border_radius=35,
            content=Column(
                controls=[
                    profile_text,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.CENTER,
            ),
        )
    )