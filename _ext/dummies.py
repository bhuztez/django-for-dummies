import unicodedata

from sphinx.writers.html import SmartyPantsHTMLTranslator


def is_cjk(c):
    c = ord(c)

    # http://www.unicode.org/versions/Unicode6.0.0/ch12.pdf
    return ( ( 0x3400  <= c <= 0x4DBF  ) or
             ( 0x4E00  <= c <= 0x9FFF  ) or
             ( 0xF900  <= c <= 0xFAFF  ) or
             ( 0x20000 <= c <= 0x2A6DF ) or
             ( 0x2A700 <= c <= 0x2B73F ) or
             ( 0x2B740 <= c <= 0x2B81F ) or
             ( 0x2F800 <= c <= 0x2FA1F ))

def ispunct(c):
    return unicodedata.category(c) == 'Po'


def is_space_required(a,b):
    if is_cjk(a) or is_cjk(b):
        return False

    return (a.isalpha() and not ispunct(b)) or (b.isalpha() and not ispunct(a))


def join_lines(s):
    lines = s.split(u'\n')
    s = lines[0]
    for line in lines[1:]:
        if s and line:
            if is_space_required(s[-1], line[0]):
                s += u' '
        s += line
    return s



class HTMLTranslator(SmartyPantsHTMLTranslator):

    def visit_Text(self, node):
        text = node.astext()
        encoded = self.encode(text)
        if self.in_mailto and self.settings.cloak_email_addresses:
            encoded = self.cloak_email(encoded)
        
        encoded = join_lines(encoded)            
        self.body.append(encoded)

