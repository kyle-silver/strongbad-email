import urwid
import itertools

from .SplashText import SplashText

class EmailScreen(urwid.WidgetWrap):
    _divider = u'─'
    _bar = u'▀'

    def __init__(self, body):
        return super(EmailScreen, self).__init__(body)
    
    def set_parent(self, parent):
        self.parent = parent
    
    def set_sbemail(self, sbemail):
        self.sbemail = sbemail
    
    def header(self, text, palette):
        text = urwid.Text(['Subject: ', text])
        text = urwid.AttrMap(text, palette)
        header = urwid.Pile([
            text,
            urwid.Divider(self._divider),
        ])
        return header

    def footer(self, palette):
        text = urwid.Text([
            (palette, 'F1'), ' Reply   ',
            (palette, 'F2'), ' Forward   ',
            (palette, 'F3'), ' Delete   ',
            (palette, 'F4'), ' Rando   ',
            (palette, 'F5'), ' Options   ',
            (palette, 'F6'), ' Help   ',
            (palette, 'ESC'), 'ape',
        ])
        footer = urwid.Pile([
            urwid.Divider(self._divider),
            text,
        ])
        return footer
    
    def keypress(self, size, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        elif key == 'f1':
            self.parent.set_screen(SplashText('REPLIED!', self.parent))
        elif key == 'f2':
            self.parent.set_screen(SplashText('FORWARDED!', self.parent))
        elif key == 'f3':
            self.parent.set_screen(SplashText('DELETED!', self.parent))
        elif key == 'f7':
            self.parent.toggle_skin()
        else:
            return super(EmailScreen, self).keypress(size, key)
