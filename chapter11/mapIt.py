#! /usr/bin/python3
# This code is part of the book Automate the Boring Stuff with Python by Al Sweigart
# mapIt.py - Launches a map in the browser using an address from the command line

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
