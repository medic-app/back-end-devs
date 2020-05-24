import random
import string
# An empty container that stores user details
user_details = []


# Function that takes user details and also generates
def user_info():
    first_name = str(input("Enter First Name: ")).lower()
    last_name = str(input("Enter Last Name: ")).lower()
    email = input("Enter Email: ")
    password = input("Enter first two letters of first name and second letter of last name: ")
    username = input("Enter Username: ")
    gen_digits = "".join(random.choice(string.digits) for i in range(4))
    final_password = f"{password}{gen_digits}"
    user_details.append(first_name)
    user_details.append(last_name)
    user_details.append(username)
    user_details.append(email)
    print(f"Your Password is: {final_password}")
    user_details.append(final_password)


# Function takes username and password, checks if its registered or not and logs user in if registered
def login():
    user1 = input("Enter Username: ")
    pass1 = input("Enter Password: ")
    if user1 in user_details and pass1 in user_details:
        print("Login Successful")
    else:
        print("Login Failed")


while True:
    print("""
WELCOME TO FASTHEALTHCARE, WHAT WOULD YOU LIKE TO DO;
1 REGISTER
2 LOGIN
3 QUIT
ENTER DESIRED OPTION NUMBER(EG, 1 OR 2) 
    """)
    welcome = input("ENTER: ")
    if welcome == "1":
        user_info()
        print(user_details)
        print("Registration Successful")
    elif welcome == "2":
        login()
    elif welcome == "3":
        print("Thanks for choosing Fasthhealthcare")
        exit()
    else:
        print("Invalid input")
