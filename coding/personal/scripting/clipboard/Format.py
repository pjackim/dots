import pyperclip
from rofi import Rofi

def bold(string):
    return f"<b>{string}</b>"

content = pyperclip.paste()
r = Rofi()
# r.error(content)

delim = r.text_entry('Delimiter')
pad = r.integer_entry("Padding")

lines = content.split('\n')
message = ""
for line in lines:
    newLine = line.split(delim)
    newLine[0] += delim
    message += f"{newLine[0]:<{pad}}{newLine[1].strip()}"
    message += "\n"


output = f"{bold('Original:')}\n\n{content}\n\n{bold('Modified:')}\n\n{message}"

r.error(output)
pyperclip.copy(message)
