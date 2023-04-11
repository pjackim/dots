import os
import pyperclip
import re
from rofi import Rofi


rofi = Rofi()

def config(conf):
    rofi.cli_conf = conf
    

def remove_patterns(input_string):
    pattern = r'<\*?>|<\/\*?>'
    return re.sub(pattern, '', input_string)

def ls(path, fileOnly=False) -> list[str]:
    files = []
    with os.scandir(path) as entries:
        for entry in entries:
            if fileOnly and not entry.is_file():
                continue
            files.append(entry.name)
    return files


def SelectFile(path="~/", r:Rofi=None, skip:str=None)-> str:
    if r is None:
        r = rofi
        r.cli_conf = "configuration {show-icons:false;}"
    file = path
    
    while os.path.isdir(file):
        file = (file + "/") if file[-1]!= "/" else file
        options = ls(file)
        
        if skip in options:
            options.remove(skip)
            
        for i in range(len(options)):
            if os.path.isdir(file + options[i]):
                options[i] = '<span foreground="#89C7C7" baseline_shift="-10pt" size="300%"></span> ' + options[i].ljust(20)
            else:
                extension = os.path.splitext(file + options[i])[1]
                icon = ""
                if extension in [".jpg", ".jpeg", ".png", ".gif"]:
                    icon = ""
                elif extension in [".py"]:
                    icon = ""
                elif extension in [".sh"]:
                    icon = ""
                options[i] = f'<span foreground="#F2DC6D" baseline_shift="-10pt" size="300%">{icon}</span> ' + options[i].ljust(20)
        
        selected = r.select("", options)
        file = file + (options[selected[0][0]][71:]).strip()
    return file