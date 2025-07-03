# Hello Android Application From Flet For Python!

# Content Of The 'main.py' File!
```python
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

# Hexadecimal Color CONSTANTS Section.
# Basic Hexadecimal Color CONSTANTS Section.
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"

BLACK = "#000000"
GRAY  = "#333333"
WHITE = "#FFFFFF"

ALPHA = GREEN

# Custom Hexadecimal Color CONSTANTS Section.
MY_RED = "#FFAAAA"
MY_GREEN = "#AAFF11"
MY_BLUE = "#0A0AFF"

# Main Program Logic Section.
def main(page: Page):

    # Main Page Window Settings Section
    page.title = WINDOW_TITLE
    page.window.width = WINDOW_WIDTH + GAP
    page.window.height = WINDOW_HEIGHT + NAVBAR_HEIGHT
    page.window.resizable = False
    page.bgcolor = GRAY
    page.update()

    # Creating Container Widget.
    container = Container(
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        bgcolor=BLACK,
        border_radius=35,
        alignment=alignment.center,
        
        content=Column([
            Text(f"{WINDOW_TITLE}", color=GREEN, size=30)],

            # Align Content (Text) To The Center Of The Container(Screen)!
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
    
    # Rendering Parent Container Widget Into A Page. 
    page.add(container)
    
# Rendering The Main Window - Starting The Program!
app(target=main)
```

# Screenshots:
![Screenshot](https://github.com/user-attachments/assets/3c9e1fc2-8e3b-484e-aa8e-9b4d6e8e02ef)
