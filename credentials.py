# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions (FINAL VERSION)
# Author: Michael Wise
# Created: 2019-10-01

def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first,last

def username(names):
    uname = names[0] + "." + names[1]
    uname = uname.lower()
    return uname

def password():
    passwd = input("Create a new password: ")
    return passwd

def isPass(passwd):
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
        if len(passwd) >= 8:
            break

    if passwd != passwd.lower() and passwd != passwd.upper():
        return True
    else:
        return False
  
def main():
    names = getName()
    uname = username(names)
    passwd = password()
    while isPass(passwd) == False:
        print("Your password needs to contain at least one upper and one lower case letter.")
        if isPass(passwd) == True:
            break
    print("The force is strong in this one…")
    print("Account configured. Your new email address is",
    uname + "@marist.edu")           

main()
