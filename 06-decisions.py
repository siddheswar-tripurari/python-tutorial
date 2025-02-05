# To get an input from user, use input method.

name = input("Enter your username: ")
password = input("Enter password: ")

if(name == "Siddhu" and password == "qwertyuiop"):
    print("Hello %s " % name)
else:
    print("Nope. Try again!")
