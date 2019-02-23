from time import time
import unicodedata
import datetime


def strip_accents(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


def format_username(firstname, lastname):
    return strip_accents("{}.{}.external".format(
        ''.join(e for e in firstname if e.isalnum()),
        ''.join(e for e in lastname if e.isalnum())
    ).lower())


def format_message(message):
    return {
        "created_at": message.get("created_at"),
        "ts_str": datetime.datetime.utcfromtimestamp(
            int(float(message.get("created_at")))
            ).strftime('%d-%m-%Y %H:%M:%S'),
        "diff_to_today": int(int(time() - int(float(message.get("created_at")))) / 60 / 60 / 24),
        "name": message.get("name"),
        "text": message.get("text")
    }


def variable_to_question(string):
    return "{} ?".format(string).replace("_", " ")
