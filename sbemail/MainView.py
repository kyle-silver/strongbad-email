import urwid

from collections import defaultdict

from .content import utils

from .screens.Lappy486 import Lappy486
from .screens.CorpyNT6 import CorpyNT6
from .screens.EmailScreen import EmailScreen

class MainView(urwid.WidgetWrap):
    # class variables
    palette = [
        ('bluescreen', 'white', 'dark blue'),
        ('lappy_accent', 'white', 'dark blue'),
        ('lappy_body', 'white', 'black'),
        ('corpy_accent', 'black', 'dark cyan'),
        ('corpy_bar', 'dark cyan', 'black')
    ]

    _skins = defaultdict(Lappy486, {
        'Lappy486': Lappy486,
        'CorpyNT6': CorpyNT6,
    })

    # init logic
    def __init__(self):
        # loop setup
        self.loop = urwid.MainLoop(
            urwid.SolidFill('#'), 
            MainView.palette, 
            unhandled_input=MainView._unhandled_input)
        # fetch sbemail
        self.sbemail = utils.random_sbemail()
        # skin setup
        self.skin = 'Lappy486'
        self.set_skin(self.skin)
        # remaining setup
        return super(MainView, self).__init__(self._w)
    
    # primary view handling
    def set_screen(self, screen):
        self.loop.widget = screen
    
    def reassert(self):
        self.loop.widget = self
    
    # skin handling
    def set_skin(self, skin: str):
        self.skin = skin
        self._w = self._skins[self.skin](self.sbemail, self)
        self.set_screen(self._w)
    
    # sbemail handling
    def new_sbemail(self):
        self.sbemail = utils.random_sbemail()
        self.set_skin(self.skin)

    # urwid wrangling
    def selectable(self):
        return True
    
    def keypress(self, size, key):
        return super(MainView, self).keypress(size, key)

    def _unhandled_input(key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
    
    # loop start
    def start(self):
        self.loop.run()
    