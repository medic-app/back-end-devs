
import string
import random
print(" WELCOME TO FAST HEALTH SOLUTION SIGN UP PAGE!!! ")
        
def signup():
    users= open('users.txt', 'a+')

    Firstname = input('Please Enter Firstname:  ')
    Lastname = input('Please Enter Lastname:  ')
    Password= input('enter first two letters of fn and second letter of lastname : ')
    password = f'{ Firstname[:2] }{Lastname[1:2] }'
    Email = input('Please Enter Email adress : ')
    Security_quote = input('Enter your security quote : ')
    while True:
        if Password !=password:
            print(' wrong input , enter a valid Password')
            signup()
            break
            
        elif Password ==password:
            print('password looks good')
            user_details=f'[Firstname: {Firstname}, Lastname: {Lastname}, Password: {Password}, Email: {Email}, Security_quote: {Security_quote}]'
            print(user_details)
            break
    users.write(Firstname)
    users.write(':')
    users.write(Lastname)
    users.write(':')
    users.write(Password)
    users.write(':')
    users.write(Email)
    users.write(':')
    users.write(Security_quote)
    users.write(':')
    users.write('\n')
    users.close()
            
       
signup()  


        
    
   