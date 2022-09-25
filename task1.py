import re

def registration():
    print("\n")
    print("Welcome please register ")
    Username = input("Enter your User Name ")
    re_username = "^[a-z A_Z]+[0-9]*[@][a-z]+[\.][a-z]{2,3}$"

    Password1 = input("Enter your Enter_Password ")
    re1_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#!$%*&? ])[A-Za-z\d@#!$%*&?]{5,16}$"
    Password2 = input("Enter your password again to confirm ")

    db = open("database.txt", "r")
    u = []
    p = []
    for i in db:
        a, b = i.split(" ")
        b = b.strip()
        u.append(a)
        p.append(b)
    if (Password1 != Password2):
        print("password do not match")
    else:
        if re.search(re_username, Username):
            if Username in u:
                print("User name exist")
            else:
                if re.search(re1_password, Password1):
                    db = open("database.txt", "a")
                    db.write(Username + " " + Password1 + "\n")
                    print("registration success")
                else:
                    print("Entered password do not match the required input format")
        else:
            print("you have entered wrong email address")

def login():
    db = open("database.txt","r")
    print("\n")
    print("Hello, Welcome to login page")
    Username = input("Enter your User Name ")
    Password1 = input("Enter your Enter_Password ")
    if not len(Username or Password1) < 1:
        u = []
        p = []
        for i in db:
            a, b = i.split(" ")
            b = b.strip()
            u.append(a)
            p.append(b)
        data = dict(zip(u,p))

        try:
            if Username in u:
                try:
                    if Password1 == data[Username]:
                        print("Login success")
                    else:
                        print("Username or Password incorrect")
                except :
                    print("Incorrect login credentials")
            else:
                print("Username doesn't exist")
                print("\n")
                registration()
        except:
            print("Username or password doesn't exist")
    else:
        print("Login Error")

def Set_New_Password():
    db = open("database.txt", "r")
    Username = input("Enter your User Name ")
    if not len(Username or Password1) < 1:
        u = []
        p = []
        for i in db:
            a, b = i.split(" ")
            b = b.strip()
            u.append(a)
            p.append(b)

        if Username in u:
            search = u.index(Username)
            a = p[search]
            new_password = input("Enter your new password ")
            new_password_checker = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#!$%*&? ])[A-Za-z\d@#!$%*&?]{5,16}$"
            if re.search(new_password_checker, new_password):
                f = open("database.txt", "r")
                text = f.read()
                text = text.replace(a, new_password)
                f.close()
                f = open("database.txt", "w")
                f.write(text)
                f.close()
                print("Your password has been changed succcessfully,please login with new password")
                login()
            else:
                print("Entered password do not match the required input format ")
        else:
            print("User name does not exist")


def Retrive__password():
    db = open("database.txt", "r")
    Username = input("Enter your user name ")
    if not len(Username or Password1) < 1:
        u = []
        p = []
        for i in db:
            a, b = i.split(" ")
            b = b.strip()
            u.append(a)
            p.append(b)

    if Username in u:
        search = u.index(Username)
        print("use " + p[search] + " as a pasword for your email_id")
        login()
    else:
        print("Username does not exist")

def Forgotpassword():

    option1 = input("Retrive__password | Set_New_Password ")
    if option1 == "Retrive__password":
        Retrive__password()
    elif option1 == "Set_New_Password":
        Set_New_Password()

def home(option = None):
    option = input("Login | Signup | Forgotpassword ")
    if option == "Login":
        login()
    elif option =="Signup":
        registration()
    elif option == "Forgotpassword":
        Forgotpassword()
    else:
        print("Invalid input")
home()


