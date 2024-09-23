def option3():              #Function to continue the program or not
    i=int(input("\n\nDO YOU WANT TO CONTINUE \n1.YES \n2.NO \n\nSELECT OPTION:"))
    try:        #Exception Handling
        if i==1:        #Option for YES
            main()
        elif i==2:      #Option for NO
            quit()
        else:
            print("PLEASE INSERT ONLY 1 - 2")       #User must enter 1 for yes or 2 for no.
            option3()
    except ValueError:
        print("PLEASE INSERT NUMBER ONLY")          #User must enter number only
        option3()

def user(i):                                        #user input of name
    if i == 1:                                      #Option for citizen
        name = input("Name         : ")             #User must enter name if citizen
        # Input for citizen
        file = open("user.txt", 'w')
        file.write(name + '\n')
        file.write(str(userIc()) + '\n')
        file.write(str(userPhone()) + '\n')
        file.close()
    else:                                           #Option for non citizen
                                                    #Input for Non Citizen
        name = input("Name         : ")         #User must enter name if non-citizen
        file = open("user.txt", 'w')
        file.write(name + "\n")
        file.write(str(userPhone()) + "\n")
        file.close()

def userIc():
    global icNum
    try:                    #Exception Handling
        ic=int(input("IC NUMBER : "))           #User must enter IC number
        icNum=str(ic)
    except:
        print("INSERT NUMBER ONLY !!")          #User must enter number only
        userIc()
    return icNum

def userPhone():
    global pNum
    try:                                        #Exception Handling
        phone=int(input("PHONE NUMBER : "))         #User must enter phone number
        pNum=str(phone)
    except:
        print("INPUT NUMBER ONLY !!")       #User must enter number only
        userPhone()
    return pNum

def option():                   #User must select option . 1 for citizen and 2 for non-citizen
    print("\n==================================")
    print("    1.citizen / 2.non-citizen     ")
    print("==================================")
    j=0
    while True:                 #Control Structure for option .

        opt = int(input("Select the option : "))        #User must enter 1 for citizen or 2 for non citizen
        ct = 0
        if opt == 1:            #Option for citizen
            ct += 1
            return ct
        elif opt == 2:          #Option for non citizen
            ct += 2
            return ct
        else:
            print("select 1 or 2 only")                 #If user enter other than 1 or 2 this messages will be happened
            ct+=3

        if ct==3:
            continue

def main():                     #All Function and the flow of program
    id = option()
    user(id)
    menu(id)
    game(id)


def menurepeat(i):
    print("===================================")
    print("                Menu               ")
    print("===================================\n")
    if i == 1:                                      #Option for citizen
        citizen = open("citizen.txt", 'r')          #Read file
        print(citizen.read())
    else:
        noncitizen = open("noncitizen.txt", 'r')        #Read file
        print(noncitizen.read())
    print("    1.Continue     2.Exit    ")          #If user select continue will go to function game . If user select exit will go to function option2.

    try:        #Exception Handling
        user = int(input("Select the option :"))        #User must enter 1 for continue or 2 for exit.
        if user == 1:           #Option for Continue
            game(i)
        elif user == 2:
            quit()
        else:       #Option for Exit
            print("Please number 1 or 2 only")          #User must enter number 1 or 2 only
            menurepeat(i)
    except ValueError:
        print("Please insert number only")          #User must enter number only
        menurepeat(i)


def menu(i):
    print("===================================")
    print("                Menu               ")
    print("===================================\n")
    if i == 1:          #Option for citizen
        citizen = open("citizen.txt", 'r')              #Read file for citizen
        print(citizen.read())
    else:               #Option for non citizen
        noncitizen = open("noncitizen.txt", 'r')        #Read file for noncitizen
        print(noncitizen.read())


def calculateNonCitizen(act, child, adult):         #Calculation for non citizen
    #Control Structure
    if child == 0:
        # Operators

        if act == 1:
            priceadult = 35 * adult
            total = priceadult
            return total

        if act == 2:
            priceadult = 20 * adult
            total = priceadult
            return total

        if act == 3:
            priceadult = 15 * adult
            total = priceadult
            return total

        if act == 12:
            priceadult = (35 + 20) * adult
            total = priceadult
            return total

        if act == 13:
            priceadult = (35 + 15) * adult
            total = priceadult
            return total

        if act == 23:
            priceadult = (20 + 15) * adult
            total = priceadult
            return total

        if act == 123:
            priceadult = (35 + 20 + 15) * adult
            total = priceadult
            return total
    else:

        if act == 1:
            priceadult = 35 * adult
            pricechild = 25 * child
            total = priceadult + pricechild
            return total

        if act == 2:
            priceadult = 20 * adult
            pricechild = 15 * child
            total = priceadult + pricechild
            return total

        if act == 3:
            priceadult = 15 * adult
            pricechild = 10 * child
            total = priceadult + pricechild
            return total

        if act == 12:
            priceadult = (35 + 20) * adult
            pricechild = (25 + 15) * child
            total = priceadult + pricechild
            return total

        if act == 13:
            priceadult = (35 + 15) * adult
            pricechild = (25 + 10) * child
            total = priceadult + pricechild
            return total

        if act == 23:
            priceadult = (20 + 15) * adult
            pricechild = (15 + 10) * child
            total = priceadult + pricechild
            return total

        if act == 123:
            priceadult = (35 + 20 + 15) * adult
            pricechild = (25 + 15 + 10) * child
            total = priceadult + pricechild
            return total


def calculateCitizen(act, child, adult):            #Calculation for citizen
    if child == 0:
    #Control Structure
        if act == 1:
            #Operators
            priceadult = 25 * adult
            total = priceadult
            return total

        if act == 2:
            priceadult = 15 * adult
            total = priceadult
            return total

        if act == 3:
            priceadult = 10 * adult
            total = priceadult
            return total

        if act == 12:
            priceadult = (25 + 15) * adult
            total = priceadult
            return total

        if act == 13:
            priceadult = (25 + 10) * adult
            total = priceadult
            return total

        if act == 23:
            priceadult = (15 + 10) * adult
            total = priceadult
            return total

        if act == 123:
            priceadult = (25 + 15 + 10) * adult
            total = priceadult
            return total
    else:
        if act == 1:
            priceadult = 25 * adult
            pricechild = 20 * child
            total = priceadult + pricechild
            return total

        if act == 2:
            priceadult = 15 * adult
            pricechild = 12 * child
            total = priceadult + pricechild
            return total

        if act == 3:
            priceadult = 10 * adult
            pricechild = 7 * child
            total = priceadult + pricechild
            return total

        if act == 12:
            priceadult = (25 + 15) * adult
            pricechild = (20 + 12) * child
            total = priceadult + pricechild
            return total

        if act == 13:
            priceadult = (20 + 10) * adult
            pricechild = (20 + 7) * child
            total = priceadult + pricechild
            return total

        if act == 23:
            priceadult = (15 + 10) * adult
            pricechild = (12 + 7) * child
            total = priceadult + pricechild
            return total

        if act == 123:
            priceadult = (25 + 15 + 10) * adult
            pricechild = (20 + 12 + 7) * child
            total = priceadult + pricechild
            return total


def calculate(i, act, child, adult, actname):               # Calculation for total price of citizen and non citizen.
    if i == 1:
        # Operators
        # If user are citizen then will get discount
        total = float(calculateCitizen(act, child, adult))
        discount = (total * 20) / 100
        netprice = total - discount
        file = open("game.txt", 'a')        #Append file for game
        file.write(str(total) + "\n")
        file.write(str(netprice) + "\n")
        file.close()

    else:
        #If user non citizen will no able to get discount.
        netprice = float(calculateNonCitizen(act, child, adult))
        file = open("game.txt", 'a')
        file.write(str(netprice) + "\n")
        file.close()

    if i == 1:
        order(actname, adult, child, total, netprice)
    else:
        #user options will be displayed again
        file = open("game.txt", 'w')
        file.write(actname + "\n")
        file.write(str(adult) + "\n")
        file.write(str(child) + "\n")
        file.write(str(netprice) + "\n")
        file.close()
        orderNonCitizen(actname, adult, child, netprice)
    option2(i)


def game(i):
    print("\nExample How To Select Activity :-\nActivity : 123 (1.SkyCab) (2.SkyRex) (3.SkyDome)")
    try:        # Exception Handling
        act = int(input("Activity : "))         # User must enter the number of activity. 1 for SkyCab , 2 for SkyRex and 3 for SkyDome.
        #Control Structure
        if act == 1:
            actname = "SkyCab"

        elif act == 2:
            actname = "SkyRex"

        elif act == 3:
            actname = "SkyDome"

        elif act == 12:
            actname = "SkyCab,SkyRex"

        elif act == 13:
            actname = "SkyCab,SkyDome"

        elif act == 23:
            actname = "SkyRex,SkyDome"

        elif act == 123:
            actname = "SkyCab,SkyRex,SkyDome"
        else:
            print("Please insert number of activity only")      # User must enter number of activity only.
            game(i)
        file = open("game.txt", 'w')        # Write file for user
        file.write(actname + "\n")
        file.close()
    except ValueError:
        print("PLEASE INSERT NUMBER ONLY")      # User must insert number only.
        game(i)
    # Control Structure
    j = 0
    while True:
        # Exception Handling
        try:
            adult = int(input("How many adult : "))         # User must enter number of adult
            j=0
        except ValueError:
            print("PLEASE INSERT NUMBER ONLY")          # User must enter number only
            j+=1

        if j==0:
            file=open("game.txt",'a')           # Append file for game
            file.write(str(adult) + "\n")
            # Control Structure
            while True:
                try:
                    child = int(input("How many child : "))         # User must enter number of child
                    j=0
                    print("="*38)
                except ValueError:
                    print("PLEASE INSERT NUMBER ONLY")      # User must enter number only
                    j+=1

                file.write(str(child) + "\n")            # Type Casting integer to string
                file.close()

                if j==0:
                    calculate(i, act, adult, child, actname)
                    main()

def order(actname, adult, child, total, netprice):              # This function will be display user order for citizen
    print("======================================")
    print("               Your order             ")
    print("======================================\n")
    print("  Activity    : " + actname)
    print("  Category    :- Adult:" + str(adult) + "Child :" + str(child))          # Type casting integer to str
    print("  Total Price : RM" + str(total))            # Type casting
    print("               -20%")
    print("======================================\n")
    print(" Net Price : RM" + str(netprice))
    print("======================================\n")


def orderNonCitizen(actname, adult, child, netprice):           #This function will be display user order for non citizen
    print("======================================")
    print("               Your order             ")
    print("======================================\n")
    print("  Activity    : " + actname)
    print("  Category    :- Adult:" + str(adult) + "Child :" + str(child))          #Type casting
    print("======================================\n")
    print(" Net Price : RM" + str(netprice))            #Type casting
    print("======================================\n")


def resit(i):           #This function will be display user resit
    print("======================================")
    print("             Your Receipt             ")
    print("======================================\n")
    file = open("user.txt", 'r')            #Read file for user
    result = file.readline()
    print("  Name        : " + result)
    if i == 1:
        result = file.readline()
        print("  Ic          : " + result)
    result = file.readline()
    print("  Phone       : " + result)

    activity = open("game.txt", 'r')        #Read file for game

    result2 = activity.readline()
    print("  Activity    : " + result2)
    result2 = activity.readline()
    result3 = activity.readline()
    print("  Category    :- Adult:" + result2 + " Child :" + result3)
    if i == 1:
        result2 = activity.readline()
        print("  Total Price : " + result2)
        print("               -20%")
    print("======================================\n")
    result2 = activity.readline()
    print(" Net Price : RM" + result2)
    print("======================================\n")
    option3()


def option2(i):         #Function for user to select option . 1 for Payment , 2 for Menu and 3 for Exit
    print("    1.Payment     2.Menu     3.Exit    ")
    try:            #Exception Handling
        user = int(input("Select the option :"))            #User must enter the number of option
        if user == 1:           #Option for Payment
            resit(i)

        elif user == 2:         #Option for Menu
            menurepeat(i)
        elif user == 3:         #Option for Exit
            quit()
        else:
            print("Please insert number 1,2,3")         #User must enter number 1,2, or 3
            option2(i)
    except ValueError:
        print("Please input number only!!!")            #User must enter number only
        return option2(i)
main()
