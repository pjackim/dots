import pyperclip
import re

content = pyperclip.paste()
content = re.sub(r'\n', ' ', content)
content = re.sub(r'  ', ' ', content)
pyperclip.copy(content)