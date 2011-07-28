### -*- coding: utf-8 -*- ####################################################

def replace_special(text):
    """Replace letter ё --> е.
    Strip leading and trailing whitespaces and " symbol
    """
    return text.strip(u' "').replace(u'ё', u'е')