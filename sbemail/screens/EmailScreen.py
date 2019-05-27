import urwid
import itertools

from .SplashText import SplashText

class EmailScreen(urwid.WidgetWrap):
    def __init__(self, content):
        return super(EmailScreen, self).__init__(content)
    
    def set_parent(self, parent):
        self.parent = parent
    
    def selectable(self):
        return True
    
    def _footer(self, palette):
        text = urwid.Text([
            (palette, 'F1'), ' Reply   ',
            (palette, 'F2'), ' Forward   ',
            (palette, 'F3'), ' Delete   ',
            (palette, 'F4'), ' Rando   ',
            (palette, 'F5'), ' Options   ',
            (palette, 'F6'), ' Help   ',
            (palette, 'ESC'), 'ape   ',
        ])
        return urwid.Pile([
            urwid.Divider('─'),
            text
        ])
    
    def keypress(self, size, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        elif key == 'f7':
            self.parent.toggle_skin()
        else:
            self.parent.set_screen(SplashText('DELETED!', self.parent))
