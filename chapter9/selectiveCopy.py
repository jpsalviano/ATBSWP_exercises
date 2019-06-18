#! /usr/bin/python3
# This code is my solution to Practice Project: Selective Copy in the book Automate the Boring Stuff with Python by Al Sweigart
# selectiveCopy.py - Searches all files for an extension in a folder tree and copies them into a new folder.
# Usage: selectiveCopy.py <extension> <source> <destination>:
#        <extension> without . (dot)
#        <source> is the folder whose tree will be searched and copied, if that's the case
#        <destination> is the folder where files from <source> will be copied into

import sys, os, shutil

# get user input: extension (ext), folder tree (src), new folder (dest)

if len(sys.argv) != 4:
    print("Usage: selectiveCopy.py <extension> <source> <destination>:\n<extension> without . (dot)\n<source> is the folder whose tree will be searched and copied, if that's the case\n<destination> is the folder where files from <source> will be copied into")
    sys.exit()
else:
    ext, src, dest = sys.argv[1], os.path.abspath(sys.argv[2]), os.path.abspath(sys.argv[3])
    if not ( os.path.isdir(src) and os.path.isdir(dest) ):      # check if folders exist
        print('Both folders must exist!')
        sys.exit()

# list all subfolders and files from <source>
# search all files for extension
# copy all matches into <destination>

for dir_path, subdir_list, file_list in os.walk(src):
    if dir_path != dest:        # avoids samefile error by not walking through <dest>
        print('Searching {}...'.format(dir_path))
        for filename in file_list:
            if filename.endswith('.' + ext):
                full_path = os.path.join(dir_path, filename)
                shutil.copy(full_path, dest)

print('Done!')
