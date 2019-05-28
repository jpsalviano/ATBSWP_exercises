#! /usr/bin/python3
# Regex Search - opens all .txt files in a folder and searches for any line that matches
# a user-supplied regular expression
# Usage: regexSearch.py <'regex'> <folderpath> - Searches and prints all lines that match a user-supplied
# regular expression in text files contained in a folder

import os, re, sys

# gets regex and folder inputs
# compiles regex
# changes cwd to input folder
if len(sys.argv) == 3:
    regex = re.compile(sys.argv[1])
    os.chdir(sys.argv[2])
else:
    print('Usage: regexSearch.py <\'regex\'> <folderpath>')
    sys.exit()

# opens all .txt files in cwd
# gets .txt files contents and passes regex
# prints line if regex is matched
for fileMatch in re.finditer(r'\S+\.txt', ' '.join(os.listdir('.'))):
    txtFile = open('./' + fileMatch.group())
    txtContent = txtFile.readlines()
    for line in txtContent:
        if regex.search(line) != None:
            if line[-1] == '\n':
                line = line[0:-1]
            print('line:\n\'' + line + '\'' + '\n[in file: ' + fileMatch.group() + ']')
    txtFile.close()
