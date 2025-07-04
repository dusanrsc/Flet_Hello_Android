# Imports Section.
# Importing Sub-Modules Section.
from flet import *

# Program Settings Section.
# CONSTANTS Section.
WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 850

NAVBAR_HEIGHT = 60
GAP = 30

WINDOW_TITLE = "Hello, Android!"
DEFAULT_FONT_SIZE = 30

# Hexadecimal Color CONSTANTS Section.
# Basic Hexadecimal Color CONSTANTS Section.
RED   = "#FF0000"
GREEN = "#00FF00"
BLUE  = "#0000FF"

BLACK = "#000000"
GRAY  = "#333333"
WHITE = "#FFFFFF"

ALPHA = GREEN

# Custom Hexadecimal Color CONSTANTS Section.
MY_RED   = "#FFAAAA"
MY_GREEN = "#AAFF11"
MY_BLUE  = "#0A0AFF"

# Default Hexadecimal CONSTANTS Colors Section.
DEFAULT_PAGE_COLOR = GRAY
DEFAULT_CONTAINER_COLOR = BLACK
DEFAULT_TEXT_COLOR = MY_GREEN

CHANGED_PAGE_COLOR = None
CHANGED_CONTAINER_COLOR = WHITE
CHANGED_FONT_COLOR = None

# Main Program Logic Section.
def main(page: Page):

    # Local Program Functions Section.
    # On Text Click Function.
    def on_text_click(event):

        # Condition For Switching Between Hello Android String Colors.
        if hello_android.color == MY_GREEN:
            hello_android.color = GREEN
        else:
            hello_android.color = MY_GREEN
        
        # Updating Changed Colors.
        hello_android.update()

    # Switch Between Modes Function.
    def switch_dark_or_light_mode(event):

        # Condition For Switching Between Two Modes.
        if container.bgcolor != CHANGED_CONTAINER_COLOR:
            container.bgcolor = CHANGED_CONTAINER_COLOR
        else:
            container.bgcolor = DEFAULT_CONTAINER_COLOR
        
        # Updating Changed Color Modes.
        container.update()

    # Main Page Window Settings Section
    page.title = WINDOW_TITLE
    page.window.width = WINDOW_WIDTH + GAP
    page.window.height = WINDOW_HEIGHT + NAVBAR_HEIGHT
    page.window.resizable = False
    page.bgcolor = GRAY
    page.update()

    # Widgets Section.
    hello_android = Text(color=DEFAULT_TEXT_COLOR, size=DEFAULT_FONT_SIZE, spans=[TextSpan(WINDOW_TITLE, on_click=on_text_click)])
    switch_mode = Switch(on_change=switch_dark_or_light_mode)

    # Creating Container Widget.
    container = Container(
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        bgcolor=DEFAULT_CONTAINER_COLOR,
        border_radius=35,
        alignment=alignment.center,
        
        content=Column([hello_android, switch_mode],

            # Align Content (Text) To The Center Of The Container(Screen)!
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
    
    # Rendering Parent Container Widget Into A Page. 
    page.add(container)
    
# Rendering The Main Window - Starting The Program!
app(target=main)
