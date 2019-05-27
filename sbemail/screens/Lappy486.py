import urwid

from .EmailScreen import EmailScreen

class Lappy486(EmailScreen):
    def __init__(self, sbemail):
        self.sbemail = sbemail
        subject = sbemail['subject'] if sbemail['subject'] is not '' else sbemail['title']
        frame = urwid.Frame(
            header=self.header(subject, palette='lappy_accent'),
            body=urwid.Filler(urwid.Text('Lappy 486')), 
            footer=self.footer(palette='lappy_accent'))
        return super(Lappy486, self).__init__(frame)
