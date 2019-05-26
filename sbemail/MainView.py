import urwid

from .screens.Lappy486 import Lappy486

class MainView(urwid.WidgetWrap):
    palette = [
        ('bluescreen', 'white', 'dark blue')
    ]

    def __init__(self, primary_screen):
        self.loop = urwid.MainLoop(
            urwid.SolidFill('#'), 
            MainView.palette, 
            unhandled_input=MainView._unhandled_input)
        self.set_primary(primary_screen)
        self.set_screen(self.primary_screen)
        return super(MainView, self).__init__(self.primary_screen)
    
    # set primary view for application
    def set_screen(self, screen):
        self.loop.widget = screen
    
    # give primary screen reference to MainView to allow for modal switching
    def set_primary(self, screen):
        screen.set_parent(self)
        # must be set for changes to persist, see WidgetWrap docs
        self._w = screen
        self.primary_screen = self._w
        self.set_screen(self._w)
    
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

