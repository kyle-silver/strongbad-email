import urwid

from .EmailScreen import EmailScreen

class Lappy486(EmailScreen):
    def __init__(self, sbemail, parent):
        self.sbemail = sbemail
        subject = sbemail['subject'] if sbemail['subject'] is not '' else sbemail['title']
        frame = urwid.Frame(
            header=self.header(subject, palette='lappy_accent'),
            body=self.body(),
            footer=self.footer(palette='lappy_accent'))
        frame = urwid.AttrMap(frame, 'lappy_body')
        return super(Lappy486, self).__init__(frame, parent)
    
    def body(self):
        text = urwid.Text(self.sbemail['body'])
        response_area = urwid.Edit('] ', multiline=True)
        return urwid.ListBox(urwid.SimpleFocusListWalker([
            text,
            urwid.Divider(self._divider),
            response_area,
        ]))
