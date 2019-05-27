import urwid
import itertools

from .content import sbemails

from .screens.Lappy486 import Lappy486
from .screens.CorpyNT6 import CorpyNT6
from .screens.EmailScreen import EmailScreen

class MainView(urwid.WidgetWrap):
    palette = [
        ('bluescreen', 'white', 'dark blue'),
        ('lappy_accent', 'white', 'dark blue'),
        ('corpy_accent', 'black', 'dark cyan'),
    ]

    def __init__(self):
        self.loop = urwid.MainLoop(
            urwid.SolidFill('#'), 
            MainView.palette, 
            unhandled_input=MainView._unhandled_input)
        self.sbemails = sbemails
        self._skins = self.get_skins()
        self.toggle_skin()
        return super(MainView, self).__init__(self._w)
    
    # set primary view for application
    def set_screen(self, screen):
        self.loop.widget = screen
    
    def get_skins(self):
        skins = [
            Lappy486(self.sbemails[0]),
            CorpyNT6(self.sbemails[0]),
        ]
        return itertools.cycle(skins)
    
    # give primary screen reference to MainView to allow for modal switching
    def set_skin(self, skin):
        skin.set_parent(self)
        # must be set for changes to persist, see WidgetWrap docs
        self._w = skin
        skin.set_sbemail(self.sbemails[0])
        self.set_screen(self._w)
    
    def toggle_skin(self):
        next_skin = next(self._skins)
        self.set_skin(next_skin)

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
