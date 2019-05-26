import urwid

class SplashText(urwid.Frame):
    def __init__(self, text, parent):
        self.parent = parent
        bt = urwid.BigText(text, font=urwid.HalfBlock7x7Font())
        bt = urwid.Padding(bt, align='center', width='clip')
        bt = urwid.Filler(bt)
        bt = urwid.AttrMap(bt, 'bluescreen')
        return super(SplashText, self).__init__(body=bt)
    
    def selectable(self):
        return True
    
    def keypress(self, size, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()
        else:
            self.parent.reassert()
