import pyperclip
import sys
import re
from collections import Counter
from rofi import Rofi
from customlibs import PrintUtil
# import PrintUtil


def count_words(string):
    return len(string.split())

def count_lines(string):
    return len(string.split('\n'))

def count_characters(string):
    return len(string)

def most_frequent_char(string:str):
    char_counts = {}
    string = string.replace(" ", "").replace("\t", "").replace("\n", "")

    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1

    return max(char_counts, key=char_counts.get)

def most_frequent_word(string):
    # Split the string into words using regular expressions
    words = re.findall(r'\w+', string.lower())
    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]

def top_ngrams(string, n):
    
    if len(string) <= 100:
        return ""
    
    words = string.split()
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    ngram_counts = {}

    for ngram in ngrams:
        ngram_counts[ngram] = ngram_counts.get(ngram, 0) + 1

    return sorted(ngram_counts, key=ngram_counts.get, reverse=True)[:3]


def bold(string):
    return f"<b>{string}</b>"

content = pyperclip.paste()

r = Rofi()
n = 3

pad = 40
msg = f"{bold('Characters:'):<{pad}} {count_characters(content):,}\n"
msg += f"{bold('Words:'):<{pad}} {count_words(content):,}\n"
msg += f"{bold('Lines:'):<{pad}} {count_lines(content):,}\n"
msg += PrintUtil.line(100) + "\n"
msg += f"{bold('Most Frequent Word:'):<{pad}} \'{most_frequent_word(content)}\'\n"
msg += f"{bold('Most Frequent Character:'):<{pad}} \'{most_frequent_char(content)}\'\n"
msg += PrintUtil.line(100) + "\n"
msg += f"{bold('Top 3 bi-grams:'):<{pad}}\n {PrintUtil.arrayTable(top_ngrams(content, 2))}\n"
msg += f"\n{bold('Top 3 tri-grams:'):<{pad}}\n {PrintUtil.arrayTable(top_ngrams(content, 3))}\n"
msg += f"\n{bold('Top 3 n-grams:'):<{pad}}\n {PrintUtil.arrayTable(top_ngrams(content, 5))}\n"

r.error(msg)