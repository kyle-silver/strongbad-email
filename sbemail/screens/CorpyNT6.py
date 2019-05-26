import urwid

from .SplashText import SplashText

class CorpyNT6(urwid.Filler):
    def __init__(self):
        text = urwid.Text('Corpy NT6')
        return super(CorpyNT6, self).__init__(text)
    
    def set_parent(self, parent):
        self.parent = parent
    
    def selectable(self):
        return True
    
    def keypress(self, size, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        else:
            self.parent.set_screen(SplashText('DELETED!', self.parent))
