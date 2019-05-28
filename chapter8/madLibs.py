#! /usr/bin/python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the words
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Usage: madLibs.py <./textfile.txt> - Opens a text file (.txt) to work with

import sys, re, os

# open text file, stores content in a variable
if len(sys.argv) != 2:
    print('Usage: madLibs.py <./textfile.txt> - Opens a text file (.txt) to work with')
    sys.exit()
else:
    textFile = open(sys.argv[1])
    textContent = textFile.read()
    textFile.close()

# this works but...
'''
# Regex locates ADJECTIVE, NOUN, ADVERB, or VERB in text content
terms = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
matches = terms.findall(textContent)

# Asks for replacement for each case
for match in matches:
    if match == 'ADJECTIVE':
        n = 'n'
    else:
        n = ''
    print('Enter a' + n + ' ' + match.lower() + ':')
    replacement = input()
    textContent = textContent.replace(match,replacement,1)

print(textContent)
newFile = open('./' + os.path.splitext(os.path.basename(sys.argv[1]))[0] + 'Replaced.txt', 'w')
newFile.write(textContent)
newFile.close()
'''

# ...let's try something different:
for match in re.finditer(r'ADJECTIVE|NOUN|ADVERB|VERB', textContent):
    if match == 'ADJECTIVE':
        n = 'n'
    else:
        n = ''
    print('Enter a' + n + ' ' + match.group().lower() + ':')
    replacement = input()
    textContent = re.sub(match.group(),replacement,textContent,1)
    
print(textContent)
newFile = open('./' + os.path.splitext(os.path.basename(sys.argv[1]))[0] + 'Replaced.txt', 'w')
newFile.write(textContent)
newFile.close()
