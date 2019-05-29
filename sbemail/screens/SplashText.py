import urwid

class SplashText(urwid.Frame):
    def __init__(self, text, parent, new_on_return=True):
        self.new_on_return = new_on_return
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
        # any keypress returns to main screen
        if self.new_on_return:
            self.parent.new_sbemail()
        self.parent.reassert()
