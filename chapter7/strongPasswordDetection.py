# Strong Password Detection

'''
A strong password is defined as one that:
-is at least 8 characters long
-contains both uppercase and lowercase characters
-has at least 1 digit

You may need to test the string against multiple regex patterns to validade its strength.
'''
import re

passRegex1 = re.compile(r'[a-z]+[A-Z]+[0-9]+')
passRegex2 = re.compile(r'[a-z]+[0-9]+[A-Z]+')
passRegex3 = re.compile(r'[A-Z]+[a-z]+[0-9]+')
passRegex4 = re.compile(r'[0-9]+[a-z]+[A-Z]+')
passRegex5 = re.compile(r'[A-Z]+[0-9]+[a-z]+')
passRegex6 = re.compile(r'[0-9]+[A-Z]+[a-z]+')

password = input()

def isPasswordStrong():
    if len(password) < 8:
        print('Password is weak')
    
