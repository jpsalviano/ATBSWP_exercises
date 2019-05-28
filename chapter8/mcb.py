#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves keyword to clipboard.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Prints all keywords to terminal.
#        py.exe mcb.pyw delete <keyword> - Deletes a keyword.
#        py.exe mcb.pyw clear - Deletes all keywords previously set.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        try:
            del mcbShelf[sys.argv[2]]
        except KeyError:
            print('keyword not found')
    else:
        print('invalid argument')
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        print(list(mcbShelf.keys()))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'clear':
        mcbShelf.clear()

mcbShelf.close()
