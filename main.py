import badge
from badge.input import Buttons

FONT_SIZE = 32

class App(badge.BaseApp):
    def on_open(self):
        badge.display.fill(1)
        badge.display.nice_text("CHERRIES!!", 50, 100 - FONT_SIZE, FONT_SIZE)
        badge.display.show()
    
    def loop(self):
        if badge.input.get_button(Buttons.SW3):
            badge.display.nice_text("Cherries cherries cherries!!", 50, 100 - FONT_SIZE, FONT_SIZE)
            badge.display.fill(1)
            badge.display.show()
