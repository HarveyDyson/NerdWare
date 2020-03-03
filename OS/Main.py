




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
    print("HELLO")
    again = True
    Password = ("Password") #(Change Me)
    while again == True:
        
        Break()
        inpt = input("ENTER YOUR PASSWORD. ")
        if inpt == Password :
            Break()
            print("WELCOME")
            again = False
            load()
            home()
        else:
            Break()
            print("INVALID PASSWORD")

def home():
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
    print("***********************************")
    print("")
    print("YOUR PROGRAMMES:")
    print("")
    print("TYPEWRITER")
    print("")
    print("CALCULATOR")
    print("***********************************")
    print("")
    print("EXIT")
    print("")
    inpt = input("ENTER YOUR COMMAND ").upper()
    if inpt == "TYPEWRITER":
        Break()
        TWXL()
    if inpt == "CALCULATOR":
        Calc()
    if inpt == "EXIT":
        login()
    else:
        print("")
        print("COMMAND '" + inpt + "' DOESN'T EXIST")
        time.sleep(2)
        home()

def TWXL():
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
    Break()
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


































































login()
