import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def format_username(firstname, lastname):
    return strip_accents("{}.{}.external".format(
        ''.join(e for e in firstname if e.isalnum()),
        ''.join(e for e in lastname if e.isalnum())
    ).lower())
