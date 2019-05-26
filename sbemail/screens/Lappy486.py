import urwid

from .SplashText import SplashText

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
            raise urwid.ExitMainLoop
        else:
            self.parent.set_screen(SplashText('DELETED!', self.parent))
