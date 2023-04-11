import pyperclip
from rofi import Rofi


def bold(string):
    return f"<b>{string}</b>"

content = pyperclip.paste()
message = ""
r = Rofi()


r.error(message)
pyperclip.copy(message)
