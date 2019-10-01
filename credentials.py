# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Michael Wise
# Created: 2019-10-01

def getName():
    global first,last
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first,last

def username():
    global uname
    uname = first + "." + last
    return uname

def password():
    passwd = input("Create a new password: ")

    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
        if len(passwd) >= 8:
            break
    return passwd

def main():
    getName()
    username()
    password()

    print("The force is strong in this one…")
    print("Account configured. Your new email address is",
    uname + "@marist.edu")

main()
