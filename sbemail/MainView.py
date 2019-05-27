import urwid
import itertools

from .screens.Lappy486 import Lappy486
from .screens.CorpyNT6 import CorpyNT6
from .screens.EmailScreen import EmailScreen

class MainView(urwid.WidgetWrap):
    palette = [
        ('bluescreen', 'white', 'dark blue'),
        ('lappy_accent', 'white', 'dark blue'),
        ('corpy_accent', 'white', 'dark cyan'),
    ]

    _skins = itertools.cycle([
        Lappy486(),
        CorpyNT6(),
    ])

    def __init__(self):
        self.loop = urwid.MainLoop(
            urwid.SolidFill('#'), 
            MainView.palette, 
            unhandled_input=MainView._unhandled_input)
        self.toggle_skin()
        return super(MainView, self).__init__(self._w)
    
    # set primary view for application
    def set_screen(self, screen):
        self.loop.widget = screen
    
    # give primary screen reference to MainView to allow for modal switching
    def set_primary(self, screen):
        screen.set_parent(self)
        # must be set for changes to persist, see WidgetWrap docs
        self._w = screen
        self.set_screen(self._w)
    
    def toggle_skin(self):
        next_skin = next(self._skins)
        self.set_primary(next_skin)

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
