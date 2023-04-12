from rofi import Rofi
import re
import os

# size = os.get_terminal_size()
# MAX_WIDTH = size.columns - 10
# MAX_HEIGHT = size.lines

# size = os.get_terminal_size()
MAX_WIDTH = 100
MAX_HEIGHT = 100

def bold(string):
    return f"<b>{string}</b>"

shapes = {
    "edge" :   "│",
    "floor" :  "─",
    "tl":      "╭",
    "tr":      "╮",
    "bl":      "╰",
    "br":      "╯",
    "tj":      "┬",
    "bj":      "┴"
}

def line(length:int = MAX_WIDTH, verbose:bool = False):
    """
    Formats a line.

    Args:
        - `length` (int, optional): The length of the line. Defaults to MAX_WIDTH.
        - `verbose` (bool, optional): If set to a truth, the output will be printed to the 
            console. Otherwise, it will be returned as a string. Defaults to False.

    Returns:
        str: The formatted line as a string, if `verbose` is False.

    Example:
        ```python
            PrintUtil.line(verbose=True)
        ```
        >>> ────────────────────────────────────────────────────
    """
    content = shapes["floor"] * length
    if verbose:
        print(content)
    else:
        return content

def arrayTable(data:list, spacing:list or int = None, verbose:bool = False):
    """
    Generates a formatted table from the input data.

    Args:
        - `data` (list): The data to be formatted.
        - `spacing` (list or int, optional): The amount of space to allocate for each 
            column in the table. If None, a default spacing of `MAX_WIDTH / len(data)` 
            is used. Defaults to None.
        - `v` (bool, optional): If set to a truth, the output will be printed to the 
            console. Otherwise, it will be returned as a string. Defaults to 0.

    Returns:
        str: The formatted table as a string, if `v` is False.

    Example:
        ```python
            arr = ["one", "two", "three", "four"]
            PrintUtil.arrayTable(arr, verbose=True)
        ```
        >>> one            two            three          four
    """
    if len(data) < 2:
        return ""
    spacing = spacing if spacing is not None else int(MAX_WIDTH / len(data))
    output = (re.sub('[\[\],\']', '', 
             ['{' + str(i) + f': <{spacing[i] if type(spacing) == list else spacing}' + '}' 
             for i in range(len(data))].__str__())).format(*data)
    if verbose:
        print(output)
    else:
        return output 
    
    
def box(message:list or str, bMax_Width:bool = False, verbose:bool = False):
    """
    Formats a message as a boxed string.

    Args:
        - `message (list or str)`: The message to be formatted. If `message` is a string, it will be split into lines using '\\n' as a delimiter.
                
        - `bMax_Width (bool, optional)`: If True, the box will be sized to fill the entire 
            width of the console window. Otherwise, it will be sized to fit the longest 
            line in `message`. Defaults to False.
        
        - `verbose` (bool, optional): If True, the output will be printed to the console. 
            Otherwise, it will be returned as a string. Defaults to False.

    Returns:
        str: The formatted box as a string, if `verbose` is falsy.

    Example:
        ```python
    PrintUtil.box("Hello World\\nMy name is Parker!", verbose=True)
        ```
            >>> ╭────────────────────╮
            >>> │ Hello World        │
            >>> │ My name is Parker! │
            >>> ╰────────────────────╯
        ```python
    arr = ["one", "two", "three", "four"]
    PrintUtil.box(arr, verbose=True)
        ```
            >>> ╭───────╮
            >>> │ one   │
            >>> │ two   │
            >>> │ three │
            >>> │ four  │
            >>> ╰───────╯
    """
    output = ""
    content = message.split('\n') if type(message) == str else message
        
    # Get the length of the longest line in the message
    max_length = MAX_WIDTH if bMax_Width else max([len(line) for line in content])
    
    # Create top edge of the box
    output = shapes["tl"] + shapes["floor"] * (max_length + 2) + shapes["tr"] + "\n"
    
    # Create each line of the message in a box
    for line in content:
        output += shapes["edge"] + " " + line.ljust(max_length) + " " + shapes["edge"] + "\n"
    
    # Create the bottom edge of the box
    output += shapes["bl"] + shapes["floor"] * (max_length + 2) + shapes["br"] + "\n"
    
    if verbose:
        print(output)
    else:
        return output
