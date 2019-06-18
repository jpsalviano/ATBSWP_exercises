#! python3
# This code is part of the book Automate the Boring Stuff with Python by Al Sweigart
# backupFileExtensionToZip.py - Copies all files of same extension in a folder into a ZIP file.

import zipfile, os

def backupFileExtensionToZip(folder, extension):
    # Create the ZIP file.
    zipFilename = '{}Files.zip'.format(extension)
    print('Creating {}...'.format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add all the files with the determined extension in folder to the ZIP file.
        for filename in filenames:
            if filename.endswith('.'+extension):
                backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupFileExtensionToZip('/home/salviano/Coding/ATBSWP_exercises/chapter9', 'py')
