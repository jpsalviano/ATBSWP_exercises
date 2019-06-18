#! /usr/bin/python3
# This code is my solution to Practice Project: Filling in the Gaps in the book
# Automate the Boring Stuff with Python by Al Sweigart
# Find all files with a given prefix in a folder, locate any gaps in the numbering and close them by renaming the later files.
# Usage: ./fillGaps.py <folder> <prefix>

import os, re, shutil

dir = '/home/salviano/Coding/ATBSWP_exercises/chapter9/fillingGaps'

seq = re.compile(r'^(spam)(\d+)(.txt)')

lst = []
for file in os.listdir(dir):
    if seq.search(file) != None:
        num = seq.search(file).group(2)
        lst.append( (int(num.lstrip('0')), file, len(num)) )

lst = sorted(lst)
for index in range(len(lst)):
    padding = lst[index][2]
    num = str(int(index) + 1)
    padded_num = num.rjust(padding, '0')
    src = os.path.join(dir, lst[index][1])
    dst = os.path.join(dir, seq.sub(r'\g<1>{}\g<3>'.format(padded_num), lst[index][1]))
    print(src, dst)
    # shutil.move(src, dst)
