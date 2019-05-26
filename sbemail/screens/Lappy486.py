import urwid

from .SplashText import SplashText
from .CorpyNT6 import CorpyNT6

class Lappy486(urwid.Filler):
    def __init__(self):
        text = urwid.Text('Lappy 486')
        return super(Lappy486, self).__init__(text)
    
    def set_parent(self, parent):
        self.parent = parent
    
    def selectable(self):
        return True
    
    def keypress(self, size, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        elif key == 's':
            self.parent.set_primary(CorpyNT6())
        else:
            self.parent.set_screen(SplashText('DELETED!', self.parent))
