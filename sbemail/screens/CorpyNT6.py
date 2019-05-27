import urwid

from .EmailScreen import EmailScreen

class CorpyNT6(EmailScreen):
    def __init__(self):
        body = urwid.Filler(urwid.Text('Corpy NT6'))
        footer = self._footer(palette='lappy_accent')
        frame = urwid.Frame(body=body, footer=footer)
        return super(CorpyNT6, self).__init__(frame)
