import urwid

from .EmailScreen import EmailScreen

class Lappy486(EmailScreen):
    def __init__(self):
        text = urwid.Text('Lappy 486')
        return super(Lappy486, self).__init__(text)
