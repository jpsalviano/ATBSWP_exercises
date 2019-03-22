'''
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats' . But your func-
tion should be able to work with any list value passed to it.
'''

def commaCode(aList):
    aString = ''
    for item in aList:
        aString += str(item)
        if aList.index(item) < (len(aList) - 2):
            aString += ', '
        elif aList.index(item) == (len(aList) - 2):
            aString += ', and '
        else:
            return aString

spam = ['apples', 'bananas', 'tofu', 'cats']

print(commaCode(spam))
