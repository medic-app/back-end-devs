import string
import random

def Forget_password():
    while True:
        try:
            feedback = input('Enter E or S for email or security quote for password recovery : ')
        except AttributeError:
            print('Invalid input, enter a proper option and try again : ')
            continue
        break
    ask_email = print('Enter your email\n')
    print('OR\n')
    ask_security_quote = print('Enter your security quote\n')
    if feedback.upper()=='E':
       ask_email = input('Enter your email : ')

    elif feedback.upper() == 'S':
        ask_security_quote = input('Enter your security quote : ')

    userfile = open('user-login.txt')
    for line in userfile:
        details = line.split(':')

        if details[3] == ask_email:
            print('Hold on a bit...\n')
            print(f'your password is {details [1]}')
            print('what else would you like to do?\n')
            start()

        elif details[4] == ask_security_quote:
            print('fetching data...')
            print(f'your password is {details [1]}')
            print('what else would you like to do?\n')
            start()

    else:
        print('Wrong information supplied, try again\n')
        Forget_password()


Forget_password()