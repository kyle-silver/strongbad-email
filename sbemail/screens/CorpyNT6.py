import urwid

from .EmailScreen import EmailScreen

class CorpyNT6(EmailScreen):
    def __init__(self):
        text = urwid.Text('Corpy NT6')
        return super(CorpyNT6, self).__init__(text)
