from flet import *
import flet_camera as fc
from profile import profile_page
import threading
import time


def workout_page(page, user, go_home=None, go_profile=None):

    page.clean()
    page.bgcolor = "#080808"
    page.padding = 0

    user_name = user["full_name"]

    # ==================================================
    # EXERCISE PAGE
    # ==================================================

    def exercise_page(workout_name, exercises):

        page.clean()

        # -----------------------------
        # TIMER VARIABLES
        # -----------------------------

        seconds = 0
        timer_running = False
        timer_thread = None

        timer_text = Text(
            "00:00",
            size=32,
            weight=FontWeight.BOLD,
            font_family="Fredoka",
            color="#E78E19",
        )

        def timer_loop():

            nonlocal seconds

            while timer_running:

                time.sleep(1)

                if timer_running:

                    seconds += 1

                    minutes = seconds // 60
                    secs = seconds % 60

                    timer_text.value = f"{minutes:02d}:{secs:02d}"

                    try:
                        page.update()
                    except:
                        break

        def start_timer(e):

            nonlocal timer_running
            nonlocal timer_thread

            if timer_running:
                return

            timer_running = True

            timer_thread = threading.Thread(
                target=timer_loop,
                daemon=True,
            )

            timer_thread.start()

        def stop_timer(e):

            nonlocal timer_running

            timer_running = False

        # ==================================================
        # CAMERA
        # ==================================================

        camera_text = Text(
            "Starting camera... 📷",
            size=13,
            font_family="Fredoka",
            weight=FontWeight.BOLD,
            color="#8D6E63",
        )

        camera = fc.Camera(
            expand=True,
            preview_enabled=True,
        )

        camera_box = Container(
            width=300,
            height=180,
            bgcolor="#333333",
            border_radius=20,
            border=Border.all(
                3,
                "#FFD1DC",
            ),
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=camera,
        )

        async def initialize_camera():

            try:

                cameras = await camera.get_available_cameras()

                if not cameras:

                    camera_text.value = "No camera found 📷"
                    page.update()

                    return

                await camera.initialize(
                    description=cameras[0],
                    resolution_preset=fc.ResolutionPreset.MEDIUM,
                    enable_audio=False,
                )

                camera_text.value = "Camera connected 📷"

                page.update()

            except Exception as ex:

                camera_text.value = "Camera unavailable 📷"

                print("CAMERA ERROR:", ex)

                page.update()

        # ==================================================
        # EXERCISE LIST
        # ==================================================

        exercise_controls = []

        for number, exercise in enumerate(
            exercises,
            start=1
        ):

            exercise_controls.append(

                Container(
                    width=300,
                    height=50,
                    bgcolor="#FFDFA8",
                    border_radius=20,
                    padding=10,

                    content=Row(
                        controls=[

                            Text(
                                f"{number}.",
                                size=15,
                                weight=FontWeight.BOLD,
                                font_family="Fredoka",
                                color="#E78E19",
                            ),

                            Text(
                                exercise,
                                size=14,
                                weight=FontWeight.BOLD,
                                font_family="Fredoka",
                                color="#333333",
                            ),

                        ],
                        spacing=10,
                    ),
                )
            )

            exercise_controls.append(
                Container(height=6)
            )

        # ==================================================
        # BUTTONS
        # ==================================================

        start_button = ElevatedButton(
            "START TIMER",
            width=145,
            height=45,
            on_click=start_timer,

            style=ButtonStyle(
                bgcolor="#A8E6A3",
                color="#333333",
                elevation=2,
                shape=RoundedRectangleBorder(
                    radius=22
                ),

                text_style=TextStyle(
                    font_family="Fredoka",
                    size=14,
                    weight=FontWeight.BOLD,
                ),
            ),
        )

        stop_button = ElevatedButton(
            "STOP",
            width=100,
            height=45,
            on_click=stop_timer,

            style=ButtonStyle(
                bgcolor="#FF7890",
                color=Colors.WHITE,
                elevation=2,
                shape=RoundedRectangleBorder(
                    radius=22
                ),

                text_style=TextStyle(
                    font_family="Fredoka",
                    size=14,
                    weight=FontWeight.BOLD,
                ),
            ),
        )

        # ==================================================
        # BACK BUTTON
        # ==================================================

        def go_back(e):

            nonlocal timer_running

            timer_running = False

            workout_page(
                page,
                user,
                go_home=go_home,
                go_profile=go_profile,
            )

        back_button = ElevatedButton(
            "← BACK",
            width=120,
            height=45,
            on_click=go_back,

            style=ButtonStyle(
                bgcolor="#A8E6A3",
                color="#333333",
                elevation=2,
                shape=RoundedRectangleBorder(
                    radius=20
                ),

                text_style=TextStyle(
                    font_family="Fredoka",
                    size=14,
                    weight=FontWeight.BOLD,
                ),
            ),
        )

        # ==================================================
        # EXERCISE CONTENT
        # ==================================================

        exercise_content = Column(

            controls=[

                Container(height=45),

                Text(
                    workout_name,
                    size=25,
                    weight=FontWeight.BOLD,
                    font_family="Fredoka",
                    color="#E78E19",
                ),

                Text(
                    f"Let's go, {user_name}!",
                    size=14,
                    weight=FontWeight.BOLD,
                    font_family="Fredoka",
                    color="#8D6E63",
                ),

                Container(height=10),

                # CAMERA
                camera_box,

                camera_text,

                Container(height=8),

                # TIMER
                timer_text,

                Row(
                    controls=[
                        start_button,
                        stop_button,
                    ],

                    alignment=MainAxisAlignment.CENTER,
                    spacing=8,
                ),

                Container(height=12),

                # EXERCISES
                Column(
                    controls=exercise_controls,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=0,
                ),

                Container(height=10),

                back_button,

                Container(height=60),
            ],

            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0,
            scroll=ScrollMode.AUTO,
        )

        # ==================================================
        # PHONE
        # ==================================================

        phone = Container(
            width=400,
            height=850,
            bgcolor="#FFF4C7",
            border_radius=35,
            content=exercise_content,
        )

        page.add(

            Container(
                expand=True,
                alignment=Alignment(0, 0),
                content=phone,
            )
        )

        page.update()

        # INITIALISE CAMERA AFTER IT HAS BEEN ADDED TO THE PAGE
        page.run_task(initialize_camera)

    # ==================================================
    # WORKOUTS
    # ==================================================

    def full_body(e):

        exercise_page(
            "FULL BODY",
            [
                "Squats — 12 reps",
                "Push Ups — 10 reps",
                "Lunges — 10 reps",
                "Plank — 30 seconds",
                "Jumping Jacks — 20 reps",
            ],
        )

    def upper_body(e):

        exercise_page(
            "UPPER BODY",
            [
                "Push Ups — 10 reps",
                "Shoulder Taps — 12 reps",
                "Arm Circles — 30 seconds",
                "Tricep Dips — 10 reps",
                "Plank — 30 seconds",
            ],
        )

    def lower_body(e):

        exercise_page(
            "LOWER BODY",
            [
                "Squats — 12 reps",
                "Lunges — 10 reps",
                "Glute Bridges — 15 reps",
                "Calf Raises — 15 reps",
                "Wall Sit — 30 seconds",
            ],
        )

    # ==================================================
    # NAVIGATION
    # ==================================================

    def open_profile(e):

        if go_profile:
            go_profile(e)

        else:
            profile_page(
                page,
                user
            )

    def open_home(e):

        if go_home:
            go_home(e)

    profile_button = ElevatedButton(
        "PROFILE",
        width=120,
        height=45,
        on_click=open_profile,

        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(
                radius=10
            ),

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
        on_click=open_home,

        style=ButtonStyle(
            bgcolor="#A8E6A3",
            color="#333333",
            elevation=2,
            shape=RoundedRectangleBorder(
                radius=10
            ),

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
            shape=RoundedRectangleBorder(
                radius=10
            ),

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

    # ==================================================
    # MAIN PAGE
    # ==================================================

    welcome_text = Text(
        f"Ready to move, {user_name}?",
        size=22,
        weight=FontWeight.BOLD,
        font_family="Fredoka",
        color="#E78E19",
    )

    subtitle = Text(
        "Choose a workout to get started!",
        size=14,
        font_family="Fredoka",
        color="#8D6E63",
        weight=FontWeight.BOLD,
    )

    # ==================================================
    # WORKOUT BUTTONS
    # ==================================================

    full_body_button = ElevatedButton(
        "FULL BODY",
        width=280,
        height=55,
        on_click=full_body,

        style=ButtonStyle(
            bgcolor="#FF7890",
            color=Colors.WHITE,
            elevation=3,
            shadow_color="#E85F78",
            shape=RoundedRectangleBorder(
                radius=28
            ),

            text_style=TextStyle(
                font_family="Fredoka",
                size=17,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    upper_body_button = ElevatedButton(
        "UPPER BODY",
        width=280,
        height=55,
        on_click=upper_body,

        style=ButtonStyle(
            bgcolor="#FF7890",
            color=Colors.WHITE,
            elevation=3,
            shadow_color="#E85F78",
            shape=RoundedRectangleBorder(
                radius=28
            ),

            text_style=TextStyle(
                font_family="Fredoka",
                size=17,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    lower_body_button = ElevatedButton(
        "LOWER BODY",
        width=280,
        height=55,
        on_click=lower_body,

        style=ButtonStyle(
            bgcolor="#FF7890",
            color=Colors.WHITE,
            elevation=3,
            shadow_color="#E85F78",
            shape=RoundedRectangleBorder(
                radius=28
            ),

            text_style=TextStyle(
                font_family="Fredoka",
                size=17,
                weight=FontWeight.BOLD,
            ),
        ),
    )

    # ==================================================
    # MAIN CONTENT
    # ==================================================

    workout_content = Column(

        controls=[

            Container(height=60),

            welcome_text,

            subtitle,

            Container(height=25),

            full_body_button,

            Container(height=10),

            upper_body_button,

            Container(height=10),

            lower_body_button,

            Container(height=20),

            Text(
                "Choose a workout to begin!",
                size=13,
                font_family="Fredoka",
                color="#8D6E63",
            ),
        ],

        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=0,
    )

    # ==================================================
    # PHONE
    # ==================================================

    phone = Container(
        width=400,
        height=850,
        bgcolor="#FFF4C7",
        border_radius=35,
    )

    phone.content = Column(

        controls=[

            Container(
                expand=True,
                content=workout_content,
                alignment=Alignment(0, 0),
            ),

            Container(
                height=70,
                content=navigation_bar,
                alignment=Alignment(0, 0),
            ),
        ],

        spacing=0,
    )

    # ==================================================
    # DISPLAY
    # ==================================================

    page.add(

        Container(
            expand=True,
            alignment=Alignment(0, 0),
            content=phone,
        )
    )

    page.update()