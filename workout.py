from flet import *
import flet_camera as fc
import asyncio
from profile import profile_page


def workout_page(page, user, go_home):

    page.clean()
    page.bgcolor = "#080808"
    page.padding = 0

    user_name = user["full_name"]

    # --------------------------------------------------
    # TIMER
    # --------------------------------------------------

    timer_text = Text(
        "00:00",
        size=32,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )

    seconds = 0
    timer_running = False

    async def timer_loop():
        nonlocal seconds

        while timer_running:
            await asyncio.sleep(1)

            if timer_running:
                seconds += 1

                minutes = seconds // 60
                remaining_seconds = seconds % 60

                timer_text.value = f"{minutes:02d}:{remaining_seconds:02d}"
                page.update()

    async def start_timer(e):
        nonlocal timer_running

        if not timer_running:
            timer_running = True
            start_button.disabled = True
            pause_button.disabled = False

            page.update()

            asyncio.create_task(timer_loop())

    async def pause_timer(e):
        nonlocal timer_running

        timer_running = False

        start_button.disabled = False
        pause_button.disabled = True

        page.update()

    async def reset_timer(e):
        nonlocal seconds, timer_running

        timer_running = False
        seconds = 0

        timer_text.value = "00:00"

        start_button.disabled = False
        pause_button.disabled = True

        page.update()

    # --------------------------------------------------
    # CAMERA
    # --------------------------------------------------

    camera = fc.Camera(
        width=280,
        height=190,
        preview_enabled=True,
    )

    camera_message = Text(
        "Starting camera...",
        size=13,
        font_family="Fredoka",
        color="#FFFFFF",
        text_align=TextAlign.CENTER,
    )

    async def setup_camera():
        try:
            cameras = await camera.get_available_cameras()

            if not cameras:
                camera_message.value = "No camera found."
                page.update()
                return

            # Try to use the front camera
            selected_camera = cameras[0]

            for cam in cameras:
                label = str(cam).lower()

                if "front" in label:
                    selected_camera = cam
                    break

            await camera.initialize(
                selected_camera,
                fc.ResolutionPreset.MEDIUM,
                enable_audio=False,
            )

            camera_message.value = ""
            page.update()

        except Exception as ex:
            camera_message.value = "Camera could not be started."
            print("Camera error:", ex)
            page.update()

    # --------------------------------------------------
    # TEXT
    # --------------------------------------------------

    welcome_text = Text(
        f"Ready to move, {user_name}?",
        size=22,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
        text_align=TextAlign.CENTER,
    )

    subtitle = Text(
        "Choose a workout to get started!",
        size=14,
        font_family="Fredoka",
        color="#8D6E63",
        text_align=TextAlign.CENTER,
    )

    # --------------------------------------------------
    # TIMER BUTTONS
    # --------------------------------------------------

    start_button = ElevatedButton(
        "START",
        width=90,
        height=42,
        on_click=start_timer,
        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(radius=20),
            text_style=TextStyle(
                font_family="Fredoka",
                size=14,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    pause_button = ElevatedButton(
        "PAUSE",
        width=90,
        height=42,
        disabled=True,
        on_click=pause_timer,
        style=ButtonStyle(
            bgcolor="#FFDFA8",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(radius=20),
            text_style=TextStyle(
                font_family="Fredoka",
                size=14,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    reset_button = ElevatedButton(
        "RESET",
        width=90,
        height=42,
        on_click=reset_timer,
        style=ButtonStyle(
            bgcolor="#FFD1DC",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(radius=20),
            text_style=TextStyle(
                font_family="Fredoka",
                size=14,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    timer_buttons = Row(
        controls=[
            start_button,
            pause_button,
            reset_button,
        ],
        alignment=MainAxisAlignment.CENTER,
        spacing=5,
    )

    # --------------------------------------------------
    # WORKOUT BUTTONS
    # --------------------------------------------------

    def workout_button(text):
        return ElevatedButton(
            text,
            width=280,
            height=50,
            on_click=lambda e: print(text + " selected"),
            style=ButtonStyle(
                bgcolor="#FF7890",
                color=Colors.WHITE,
                elevation=3,
                shadow_color="#E85F78",
                shape=RoundedRectangleBorder(radius=28),
                text_style=TextStyle(
                    font_family="Fredoka",
                    size=16,
                    weight=FontWeight.BOLD,
                ),
            ),
        )

    full_body_button = workout_button("FULL BODY")
    upper_body_button = workout_button("UPPER BODY")
    lower_body_button = workout_button("LOWER BODY")

    # --------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------

    def open_profile(e):
        profile_page(
            page,
            user,
            go_home=go_home,
            go_workout=lambda e: workout_page(
                page,
                user,
                go_home,
            ),
        )

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
        on_click=go_home,
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
        on_click=lambda e: None,
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
    # PHONE CAMERA / NOTCH
    # --------------------------------------------------

    phone_camera = Container(
        width=120,
        height=32,
        bgcolor="#000000",
        border_radius=20,
        ignore_interactions=True,
    )

    # --------------------------------------------------
    # MAIN CONTENT
    # --------------------------------------------------

    workout_content = Column(
        controls=[
            Container(height=60),

            welcome_text,

            subtitle,

            Container(height=10),

            # LIVE CAMERA
            Container(
                width=280,
                height=190,
                bgcolor="#333333",
                border_radius=20,
                border=Border.all(3, "#FFD1DC"),
                alignment=Alignment(0, 0),
                content=Stack(
                    controls=[
                        camera,

                        Container(
                            alignment=Alignment(0, 0),
                            content=camera_message,
                        ),
                    ],
                ),
            ),

            Container(height=8),

            timer_text,

            timer_buttons,

            Container(height=12),

            full_body_button,

            Container(height=6),

            upper_body_button,

            Container(height=6),

            lower_body_button,

            Container(height=10),
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
            workout_content,

            Container(
                alignment=Alignment(0, 0.88),
                content=navigation_bar,
            ),

            Container(
                alignment=Alignment(0, -0.95),
                content=phone_camera,
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

    # Start camera after page has been added
    asyncio.create_task(setup_camera())