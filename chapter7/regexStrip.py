# Regex Version of strip()

'''
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argu-
ment to the function will be removed from the string.
'''

import re

def reStrip(strToBeModified, strToBeStripped = r'\s'):
    strRegexStart = r'^[' + strToBeStripped + ']*'
    strRegexEnd = r'[' + strToBeStripped + ']*$'
    regexStart = re.compile(strRegexStart)
    regexEnd = re.compile(strRegexEnd)
    modifiedStr = regexStart.sub('', strToBeModified)
    modifiedStr = regexEnd.sub('', modifiedStr)
    return modifiedStr
