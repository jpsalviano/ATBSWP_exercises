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
passRegex4 = re.compile(r'[A-Z]+[0-9]+[a-z]+')
passRegex5 = re.compile(r'[0-9]+[A-Z]+[a-z]+')
passRegex6 = re.compile(r'[0-9]+[a-z]+[A-Z]+')


def passRegexes(password):
    if passRegex1.search(password) != None:
        return True
    if passRegex2.search(password) != None:
        return True
    if passRegex3.search(password) != None:
        return True
    if passRegex4.search(password) != None:
        return True
    if passRegex5.search(password) != None:
        return True
    if passRegex6.search(password) != None:
        return True
    

def isPasswordStrong():
    while True:
        password = input('Type a password:\n')
        if len(password) >= 8:
            if passRegexes(password) == True:
                passwordConfirmation(password)
                break
            else:
                print('Your password must contain both uppercase and lowercase letters, and at least 1 digit.')
        else:
            print('Your password must be at least 8 characters long.')


def passwordConfirmation(password):
    confirmPass = input('Type your password again:\n')
    if confirmPass == password:
        print('Your password has been set.')
    else:
        print('Passwords typed are different.')
        isPasswordStrong()
        

isPasswordStrong()
