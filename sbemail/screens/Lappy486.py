import urwid

class Lappy486(urwid.Filler):
    def __init__(self):
        text = urwid.Text('Lappy 486')
        return super(Lappy486, self).__init__(text)
    
    def set_parent(self, parent):
        self.parent = parent
