import random
import re


def check_email():
    import re

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(regex, Email):
        validate()
    else:
        print("Invalid Email")

def validate():
    if len(FirstName) < 5:
        print("Name must be 5 characters")
    if len(LastName) < 5:
        print("Last Name must be more than 5 characters")
    if len(password) < 6:
        print("Password must be more than 6 characters")
    else:
        Add_user()


def Add_user():
    user_info = {
            'FirstName': FirstName,
            'LastName': LastName,
            'Email': Email,
            'password': password
        }

    with open('users.txt', 'w') as f:
        f.write(str(user_info))
        print(f"Welcome: {FirstName}")


print("Input the following details to Register")
FirstName = input("Enter your First Name: ")
LastName = input("Enter your Last Name: ")
Email = input("Enter your Email Address: ")
password = input("Enter your password: ")

#Check Email and add user
check_email()




