def sign_up():
    import getpass
    first_name=input('What is your first name? ')
    last_name=input('What is your last name? ')
    email=input('what is your email address? ')
    #password=getpass.getpass('pasword?')
    
    with open('health_user.txt', 'w+') as file:
        file.write("first name: %s \n" %first_name)
        file.write("last name: %s \n" %last_name)
        file.write("email: %s \n" %email)
        file.close()

    
    return first_name, last_name, email
    
	

def check_email():
    import re
    
    a,b,email=sign_up()
    
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(regex, email):
        return('Valid Email')
    else:
        return('Invalid')


def all_sign_up():
    
    while check_email() == 'Invalid':
        print('try again')
    else:
        print('okay')
        
        
all_sign_up()    