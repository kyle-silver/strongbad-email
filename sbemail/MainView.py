import urwid

from .screens.Lappy486 import Lappy486

class MainView(urwid.WidgetWrap):
    palette = [
        ('bluescreen', 'white', 'dark blue')
    ]

    def __init__(self, primary_screen):
        # loop setup
        placeholder = urwid.SolidFill('#')
        self.loop = urwid.MainLoop(placeholder, MainView.palette, 
            unhandled_input=MainView._unhandled_input)
        # give primary screen reference to MainView to allow for modal switching
        self.primary_screen = primary_screen
        self.primary_screen.set_parent(self)
        # set primary view for application
        self.set_screen(self.primary_screen)
        return super(MainView, self).__init__(self.primary_screen)
    
    def set_screen(self, screen):
        self.loop.widget = screen
    
    def reassert(self):
        self.loop.widget = self
    
    def selectable(self):
        return True
    
    def keypress(self, size, key):
        return super(MainView, self).keypress(size, key)

    def _unhandled_input(key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
    
    def start(self):
        self.loop.run()

