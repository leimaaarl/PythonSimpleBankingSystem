



print("---Welcome to Bank---")

outBal = 10000

userName = input("Enter your username: ")
passWord = input("Enter your password: ")

print("--Welcome to Verification--")

userVer = input("Enter your username: ")
passVer = input("Enter your password: ")

if (userName == userVer and passWord == passVer):
    print("Logged In, Welcome "+ userName)

    def bank():

        print("---Welcome to Dashboard---")
        print("")

        while True: 

            print("[1]Balance [2]Deposit [3]Withdraw [4]Exit")
            choice = int(input("Choice: "))
            if (choice == 1):
                checkBal()
            elif (choice == 2):
                deposit()
            elif (choice == 3):
                withdraw()
            elif (choice == 4):
                exit()
                break


    def checkBal():
        global outBal
        print("Your Balance is "+ str(outBal))


    def withdraw():
        global outBal
        withAm = int(input("Enter amount: "))    
        if (withAm < outBal):
            if(withAm %100 == 0):
                outBal = outBal - withAm
                print("Transaction Succesful, Your new Balance  is "+ str(outBal))
            else:
                print("Amount Error, Coins Detected, Please Try again")
                withAm2 = int(input("Enter amount: "))
                if(withAm2 %100 == 0):
                    outBal = outBal - withAm2
                    print("Transaction Succesful, Your new Balance  is "+ str(outBal))


    def deposit():
        global outBal
        depAm = int(input("Enter amount: "))
        outBal = outBal + depAm
        print(" Transaction Sucessful, Your new Balance is " + str(outBal))


    def exit():
        print("Thank you for using Bank")


    bank()
        

else:
    Attempts  = 0
    Limit = 3

    while(Attempts < Limit):
         Attempts+=1
         print("Logged in Failed, Please try again")
         print("You have "+ str(Attempts) + " out of "+ str(Limit))
         userVer1 = input("Enter your username: ")
         passVer1 = input("Enter your password: ")

         if(userVer1 == userName and passVer1 == passWord):
            print("Logged In, Welcome "+ userName)
            Attempts +=3
            def bank():

                print("---Welcome to Dashboard---")
                print("")


                while True:

                    print("[1]Balance [2]Deposit [3]Withdraw [4]Exit")
                    choice = int(input("Choice: "))
                    if (choice == 1):
                        checkBal()
                    elif (choice == 2):
                        deposit()
                    elif (choice == 3):
                        withdraw()
                    elif (choice == 4):
                        exit()
                        break


            def checkBal():
                global outBal
                print("Your Balance is "+ str(outBal))


            def withdraw():
                global outBal
                withAm = int(input("Enter amount: "))    
                if (withAm < outBal):
                    if(withAm %100 == 0):
                        outBal = outBal - withAm
                        print("Transaction Succesful, Your new Balance  is "+ str(outBal))
                    else:
                        print("Amount Error, Coins Detected, Please Try again")
                        withAm2 = int(input("Enter amount: "))
                        if(withAm2 %100 == 0):
                            outBal = outBal - withAm2
                            print("Transaction Succesful, Your new Balance  is "+ str(outBal))


            def deposit():
                global outBal
                depAm = int(input("Enter amount: "))
                outBal = outBal + depAm
                print(" Transaction Sucessful, Your new Balance is " + str(outBal))


            def exit():
                print("Thank you for using Bank")
            
        
            bank()


        
         if(Attempts == 3):
             print("Attempts Limit Reached")


