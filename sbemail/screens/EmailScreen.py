import urwid
import itertools

from .SplashText import SplashText

class EmailScreen(urwid.Filler):
    def __init__(self, text):
        return super(EmailScreen, self).__init__(text)
    
    def set_parent(self, parent):
        self.parent = parent
    
    def selectable(self):
        return True
    
    def keypress(self, size, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        elif key == 'ctrl s':
            next_skin = self.parent.next_skin()
            self.parent.set_primary(next_skin)
        else:
            self.parent.set_screen(SplashText('DELETED!', self.parent))