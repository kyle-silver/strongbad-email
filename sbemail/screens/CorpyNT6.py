import urwid

from .EmailScreen import EmailScreen

class CorpyNT6(EmailScreen):
    def __init__(self, sbemail):
        self.sbemail = sbemail
        subject = sbemail['subject'] if sbemail['subject'] is not '' else sbemail['title']
        frame = urwid.Frame(
            header=self.header(subject, palette='corpy_accent'),
            body=urwid.Filler(urwid.Text('Corpy NT6')), 
            footer=self.footer(palette='corpy_accent'))
        return super(CorpyNT6, self).__init__(frame)
