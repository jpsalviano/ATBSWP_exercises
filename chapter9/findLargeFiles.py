#! /usr/bin/python3
# This code is my solution to Practice Project: Deleting Unneeded Files in the book Automate the Boring Stuff with Python by Al Sweigart
# findLargeFiles.py - Search for files larger than a user determined size in a folder tree and print their absolute paths.
# Usage: findLargeFiles.py <folder> <size> - <folder> is the root of the folder tree to be searched
#                                        <size> an integer representing in bytes the minimum size of files to have their name printed

import sys, os

# get user inputs and store in variables: folder and size
if len(sys.argv) != 3:
    print('''Usage: findLargeFiles.py <folder> <size>\n<folder> is the root of the folder tree to be searched
<size> an integer representing in bytes the minimum size of files to have their name printed''')
    sys.exit()
    
if os.path.isdir(sys.argv[1]):       # check if folder exists
    folder = os.path.abspath(sys.argv[1])
else:
    print('Folder does not exist!')
    sys.exit()

if sys.argv[2].isdigit():       # check if size is integer
    size = int(sys.argv[2])
else:
    print('Size must be a whole number.')
    sys.exit()

# gets formatted (mb) size
# source: http://code.activestate.com/recipes/578019-bytes-to-human-human-to-bytes-converter/
def GetHumanReadable(size,precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1 #increment the index of the suffix
        size = size/1024.0 #apply the division
    return "%.*f%s"%(precision,size,suffixes[suffixIndex])

# list all files larger than <size> in <folder> tree
# print their absolute paths
for dir_path, subdir_list, file_list in os.walk(folder):
    for filename in file_list:
        full_path = os.path.join(dir_path, filename)
        fileSize = os.path.getsize(full_path)
        if fileSize >= size:
            print(str(full_path) + '\n-- size: ' + GetHumanReadable(fileSize))
