from rofi import Rofi
import PrintUtil
r = Rofi()


arr = ["one", "two", "three", "four"]
PrintUtil.arrayTable(arr, verbose=True)
PrintUtil.box("Hello World\nMy name is Parker!", verbose=True)
PrintUtil.box(arr, verbose=True)
PrintUtil.line(verbose=True)

# r.error('I cannot let you do that.')

# validator = lambda s: (s, None) if len(s) > 6 else (None, "Too short!")
# r.generic_entry('Enter a 7-character or longer string: ', validator)


# options = ['Red', 'Green', 'Blue', 'White', 'Silver', 'Black', 'Other']
# index, key = r.select('What colour car do you drive?', options)

# options = ['Red', 'Green', 'Blue', 'White', 'Silver', 'Black', 'Other']
# index, key = r.select('What colour car do you drive?', options, key5=('Alt+n', "I don't drive"))
# print(index, key)

# r.text_entry('What are your goals for this year? ', message='Be <b>bold</b>!')

# msg = Rofi.escape('Format: <firstname> <lastname>')
# r.text_entry('Enter your name: ', message=msg)

