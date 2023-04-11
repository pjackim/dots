import sys
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
from rofi import Rofi
import os
import pyperclip


def list_files(path, fileOnly=False):
    files = []
    with os.scandir(path) as entries:
        for entry in entries:
            if fileOnly and not entry.is_file():
                continue
            files.append(entry.name)
    return files

def get_system_font_name(otf_file):
    font = TTFont(otf_file)
    name_table = font["name"]
    system_font_name = ""

    for record in name_table.names:
        if record.nameID == 4:  # Name ID 4 is the full font name
            system_font_name = record.toUnicode()
            break

    font.close()
    return system_font_name

def print_otf_characters(font_file):
    font = TTFont(font_file)
    cmap = font.getBestCmap()
    output = []
    for codepoint, glyphname in cmap.items():
        character = chr(codepoint)
        unicode_name = Unicode[codepoint]

        output.append(f'<big>{character:<2}</big><span face="IosevkaTerm Nerd Font Mono">{glyphname}</span>')
    return output


r = Rofi()
r.theme = "/home/pjackim/.config/rofi/blurry_full.rasi"
file = "/home/pjackim/.fonts"

while os.path.isdir(file):
    file = file + "/"
    options = list_files(file)
    selected = r.select("Font File", options)
    file = file + options[selected[0][0]]
    

print(file)
font_name = get_system_font_name(file)
print(font_name)

if ("Awesome" in font_name):
    font_name = "Font Awesome 6 Pro"
elif ("Iosevka" in font_name):
    font_name = "IosevkaTerm Nerd Font Mono"

font = f'font:  "{font_name} 20";'
config = 'configuration {show-icons:false;} * {'+font+'}'
r.cli_conf = config

options = print_otf_characters(file)
index, key = r.select('Glyph', options)
selected = str(options[index[0]])
glyph = selected[selected.index(">")+1:selected.index("</")-1]
pyperclip.copy(glyph)
