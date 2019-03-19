# The Collatz Sequence - page 77

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

def tryCollatz():
    newValue = collatz(userInput)
    while newValue != 1:
        newValue = collatz(newValue)

while True:
    try:
        userInput = int(input())
        break
    except:
        print('Input has to be an integer bigger than 0.')
        continue

tryCollatz()
