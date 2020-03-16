




def load():
    print("")
    print("LOADING...")
    time.sleep(5)
    print("")

def cont():
    time.sleep(1)
    print("")
    print("")
    input("PRESS ENTER TO CONTINUE.")

def Break():
    time.sleep(1)
    print("")

def login():
    global time
    import time
    f = open("NerdWARE TITLE.txt", "r")
    print(f.read())
    Break()
    input("                          PRESS ENTER TO START ")
    Break()
    f = open("password.txt", "r")
    password = f.readline()
    print("HELLO")
    time.sleep(5)
    again = True
    Password = password #(Change Me)
    x = 0
    while again == True:
        BB()
        Break()
        inpt = input("ENTER YOUR PASSWORD. ")
        if inpt == Password :
            Break()
            BB()
            print("WELCOME")
            again = False
            load()
            home()
        else:
            Break()
            BB()
            print("INVALID PASSWORD")
            time.sleep(3)
            x = x + 1
            if x == 3:
                BB()
                print("INVALID PASSWORD ENTERED TOO MANY TIMES")
                print("")
                print("SHUTTING DOWN")
                time.sleep(5)
                BB()
                time.sleep(3)
                exit()
def home():
    BB()
    print("***********************************")
    print("")
    print("YOUR PROGRAMMES:")
    print("")
    print("TYPEWRITER")
    print("")
    print("CALCULATOR")
    print("")
    print("SETTINGS")
    print("***********************************")
    print("")
    print("LOG OUT")
    print("")
    print("SHUTDOWN")
    print("")
    inpt = input("ENTER YOUR COMMAND ").upper()
    if inpt == "TYPEWRITER":
        Break()
        TWXL()
    if inpt == "CALCULATOR":
        Calc()
    if inpt == "LOG OUT":
        login()
    if inpt == "SETTINGS":
        settings()
    if inpt == "SHUTDOWN":
        print("")
        print("SHUTTING DOWN")
        time.sleep(5)
        BB()
        time.sleep(3)
        exit()
    else:
        print("")
        print("COMMAND '" + inpt + "' DOESN'T EXIST")
        time.sleep(2)
        home()

def TWXL():
    BB()
    f = open("TYPEWRITERXL", "r")
    print(f.read())
    load()
    Break()
    print("TO ADD MORE TO THE PAD , JUST START WRITING. ")
    Break()
    TEXT = input("").upper()
    f = open("PAD", "a")
    f.write(TEXT + "\n" + "\n")
    f.close()
    Break()
    print("APPENDING TO PAD...")
    time.sleep(6)
    print("")
    print("APPENDED")
    Break()
    print("YOUR PAD:")
    print("")
    f = open("PAD", "r")
    print(f.read())
    Break()
    input("PRESS ENTER TO GO BACK TO HOME.")
    home()    


def Calc():
    BB()
    print("********************")
    print("                    ")
    print("    CALCULATOR      ")
    print("                    ")
    print("********************")
    load()
    print("")
    input("PRESS ENTER TO BEGIN")
    print("")
    CalcHome()
    
def CalcHome():
    BB()
    print("******")
    print("HELP")
    print("******")
    print("")
    print("+ = ADD")
    print(" - = SUBTRACT")
    print("* = MULTIPLY")
    print("/= DIVIDE")
    print("")
    print("EXIT")
    print("******")
    print("")
    inpt = input("ENTER YOUR COMMAND ").upper()
    Break()
    if inpt == "+":
        add()
    if inpt == "-":
        sub()
    if inpt == "*":
        mul()
    if inpt == "/":
        div()
    if inpt == "EXIT":
        home()
    else:
        print("")
        print("COMMAND '" + inpt + "' DOESN'T EXIST")
        CalcHome()


def add():
    num1 = int(input("NUMBER 1: "))
    print("+")
    num2= int(input("NUMBER 2: "))
    print("=")
    num3 = num1 + num2
    print(num3)
    print("************")    
    input("")
    CalcHome()

def sub():
    num1 = int(input("NUMBER 1: "))
    print("-")
    num2= int(input("NUMBER 2: "))
    print("=")
    num3 = num1 - num2
    print(num3)
    print("************")    
    input("")
    CalcHome()

def mul():
    num1 = int(input("NUMBER 1: "))
    print("*")
    num2= int(input("NUMBER 2: "))
    print("=")
    num3 = num1 * num2
    print(num3)
    print("************")    
    input("")
    CalcHome()

def div():
    num1 = int(input("NUMBER 1: "))
    print("/")
    num2= int(input("NUMBER 2: "))
    print("=")
    num3 = num1 / num2
    print(num3)
    print("************")    
    input("")
    CalcHome()



def settings():
    BB()
    print("************")
    print("*          *")
    print("* SETTINGS *")
    print("*          *")
    print("************")
    time.sleep(5)
    BB()
    print("****************")    
    print("")
    print("CHANGE PASSWORD")
    print("")
    print("EXIT")
    print("****************")
    print("")
    inpt = input("ENTER YOUR COMMAND ").upper()
    if inpt == "CHANGE PASSWORD" or "CHANGEPASSWORD":
        passwordchange()
    if inpt == "EXIT":
        settings()
    else:
        print("")
        print("COMMAND '" + inpt + "' DOESN'T EXIST")
        time.sleep(2)
        home()

def passwordchange():
    BB()
    Break()
    print("PASSWORD CHANGE")
    Break()
    file = open("password.txt", "r")
    password = file.readline()
    file.close()
    x = 0
    again = True
    while again == True:
        Break()
        inpt = input("ENTER OLD PASSWORD ")
        if inpt == password :
            print("")
            print("CORRECT PASSWORD")
            again = False
            f = open("password", "w")
            print("")
            inpt = input("ENTER NEW PASSWORD ")
            f.write(inpt)
            f.close()
            time.sleep(3)
            print("")
            print("PASSWORD SUCCESSFULLY CHANGED")
            time.sleep(5)
            settings()

        else:
            Break()
            BB()
            print("INVALID PASSWORD")
            time.sleep(3)
            x = x + 1
            if x == 3:
                BB()
                print("INVALID PASSWORD ENTERED TOO MANY TIMES")
                print("")
                home()









    
def BB():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")


























































login()
