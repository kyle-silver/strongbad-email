import urwid

from .EmailScreen import EmailScreen

class Lappy486(EmailScreen):
    def __init__(self):
        body = urwid.Filler(urwid.Text('Lappy 486'))
        footer = self._footer(palette='lappy_accent')
        frame = urwid.Frame(body=body, footer=footer)
        return super(Lappy486, self).__init__(frame)
