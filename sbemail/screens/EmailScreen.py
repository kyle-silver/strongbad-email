import urwid
import itertools

from .SplashText import SplashText

class EmailScreen(urwid.WidgetWrap):
    _divider = u'─'
    _bar = u'▀'
    _skins = itertools.cycle([
        'CorpyNT6',
        'Lappy486', 
    ])

    def __init__(self, body, parent):
        self.parent = parent
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
        nbsp = '\u00a0'
        text = urwid.Text([
            (palette, 'F1'), f'{nbsp}Reply   ',
            (palette, 'F2'), f'{nbsp}Forward   ',
            (palette, 'F3'), f'{nbsp}Delete   ',
            (palette, 'F4'), f'{nbsp}Rando   ',
            (palette, 'F5'), f'{nbsp}Options   ',
            (palette, 'F6'), f'{nbsp}Help   ',
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
        elif key == 'f4':
            self.parent.new_sbemail()
        elif key == 'f7':
            self.parent.set_skin(next(self._skins))
        else:
            return super(EmailScreen, self).keypress(size, key)
