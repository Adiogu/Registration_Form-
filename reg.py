import random


def PASSWORD(LENGHT=7):

    password = input("Enter your password : ")

    count = len(password)
    
    if count >= LENGHT:
        print("Correct")
        print(password)
    elif count < LENGHT:
        print("Invalid password.Try Again")
        PASSWORD()
    else:
        print("INCORRECT PASSWORD")


MEMORY = []


def USER_DATA(size=5):


    while True:
        print("Kindly fill the form below.")

        line = 30 * "="
        print(line)

        print(".REGISTRATION FORM.")
        FirstName = str(input("Firstname :    ")).upper()
        LastName = str(input("Lastname :  ")).upper()
        Email = str(input("Email :   "))

        F = FirstName[0:2]
        L = LastName[-2:]
        Alphabets = 'abcdefghijklmnopqrstuvwxyz0123456789'
        game = "" .join(random.choice(Alphabets.upper())for x in range(size))
        password = F + game + L
        print("YOUR PASSWORD = " + password )


        print("Are you ok with your login password\n(Y/N)")

        select = input("ENTER : ").upper()

        if select == 'Y':
            print('Registration successful\nWelcome to HNG-TECH {}'.format(FirstName + ' ' + LastName))
        elif select == 'N':
            print("TYPE IN THE PASSWORD OF YOUR CHOICE\nAND IT MUST BE MORE THAN 7 CHARACTERS.")
            PASSWORD()
        else:
            print("INVALID SELECTION\nTRY AGAIN.")

        saved = ('NAME : {} \n'
                 'Email : {} \n'
                 'Password : {} \n'
                 '\n'.format(FirstName + ' ' +LastName,Email,password))


        container = MEMORY.append(saved)


        select = input("ARE YOU DONE INPUTTING ALL RECORDS.(Y/N)\nENTER : ").upper()
        if select == 'Y':
            print("Data are saved\n")
            for x in MEMORY:
                print(x)
        elif select == 'N':
            USER_FORM()
        else:
            print("INVALID INPUT SELECTED = {} ".format(select))
        break


USER_DATA()
