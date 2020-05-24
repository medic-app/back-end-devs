import re

first_Name = input('first_name: ')

if len(first_Name) < 4:
    print('Name must be at least 3 charaters')
elif len(first_Name) > 20:
    print('Name must be a maxmium of 15 characters 😙')
else:
    print('Name looks good 🙂')


last_name = input('last_name: ')

if len(last_name) < 3:
    print('Name must be at least 3 charaters 😙')
elif len(last_name) > 20:
    print('Name must be a maxmium of 15 characters')
else:
    print("Name looks good")

phone = input('phone: ')

if len(phone) < 6:
    print("Phone Number must be at least 6 in length")
elif len(phone) > 11:
    print('Phone number must not be longer than 11.')
else:
    print('Good valid Number! 🙂')

    Address = input('Enter Address: ')

    if len(Address) < 10:
        print('Please too short characters 😫')
    elif len(Address) < 25:
        print('Too long Characters')
    else:
        print('Good characters 🙂')


def check_email():
    import re

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(regex, check_email):
        check_email()
    else:
        print("Invalid Email")


Email = input("Enter your Email Address: ")
check_email()
