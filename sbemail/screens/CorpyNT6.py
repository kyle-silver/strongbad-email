import urwid

from .EmailScreen import EmailScreen

class CorpyNT6(EmailScreen):
    def __init__(self, sbemail, parent):
        self.sbemail = sbemail
        subject = sbemail['subject'] if sbemail['subject'] is not '' else sbemail['title']
        frame = urwid.Frame(
            header=self.header(subject, palette='corpy_accent'),
            body=self.body(), 
            footer=self.footer(palette='corpy_accent'))
        return super(CorpyNT6, self).__init__(frame, parent)
    
    def body(self):
        text = urwid.Text(self.sbemail['body'])
        response_area = urwid.Edit('> ', multiline=True)
        return urwid.ListBox(urwid.SimpleFocusListWalker([
            text,
            urwid.AttrMap(urwid.Divider(self._bar), 'corpy_bar'),
            response_area,
        ]))
