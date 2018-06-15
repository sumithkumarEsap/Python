import re

#using regular expressions and its inbuilt function to check for the conditons stated
def password_check(password):
    check = True
    while check:
        #will check for the length of the password,it should be between 6 and 12
        if (len(usr_inp) not in range(6, 16)):
            break
        # will check if the password contains any digit

        elif not re.search("[0-9]", usr_inp):
            break
        #will check if the password contains any alphaber in lower case

        elif not re.search("[a-z]", usr_inp):
            break

        # will check if the password contains any alphaber in upper case
        elif not re.search("[A-Z]", usr_inp):
            break
        # will check if the password contains any special char
        elif not re.search("[$@!*]", usr_inp):
            break
        else:
            print("Strong Password")
            check = False
            break
#if any of the above conditions fail then it will go through this
    if check:
        print("weak Password")

#asking for user password
usr_inp=input("enter your password")
#calling password_check function on user given password
password_check(usr_inp)