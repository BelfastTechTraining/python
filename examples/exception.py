x = 3
try:
    print(x / 0)
except ZeroDivisionError:
    print('You\'re trying to print by zero, this isnt allowed!')
