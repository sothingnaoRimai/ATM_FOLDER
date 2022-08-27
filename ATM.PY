print("Welcome to SBI")
print("Swipe your card here:")
language=input(" enter your language   ")
if language=="english":
    pin=input("enter your pin   ")
    amount=300000
    transaction=("balance enquiry","withdraw money","deposit","change your pin","transfer money","quit")
    if pin==pin:
        if len(pin)==4:
            print("choose your transaction:")
            print("1.balance enquiry")
            print("2.witprhdraw money")
            print("3.deposit")
            print("4.change your pin")
            print("5.transfer money")
            print("6.quit")
            trans=input("transaction:")
            if trans=="balance enquiry":
                swipe=input("Do you want to swipe  ")
                if swipe=="yes":
                    print( amount," Thanks for using SBI bank")
                else:
                    print("thanks for using SBI Bank")
            elif trans=="withdraw money":
                amount1=int(input("enter your amount to proceed  "))
                if amount1>=0 and amount1<=300000:
                    print("collect your cash!",amount-amount1, "is left in your account!thanks for using SBI Bank")
                else:
                    print("enter valid amount to proceed")
            elif trans=="deposit":
                amount2=int(input("enter the amount to deposit  "))
                if amount2>=0:
                    print("your deposit is succesful!",amount+ amount2 ,"is in your account, Thanks for using SBI Bank")
                else:
                    print("enter valid amount to Deposit")
            elif trans=="change your pin":
                change_pin=input("enter your new pin,sir  ")
                if  len(change_pin)==4:
                    print("Your pin is successfully change! Thanks for using SBI Bank!")
                else:
                    print("enter a valid pin that `ffwfaddxcyis equal to four digit")
            elif trans=="transfer money":
                transfer_money=int(input("enter the amount  "))
                if transfer_money>=0:
                    print("your transaction is successful", amount-transfer_money,"is left in your account! thanks for using SBI Bank!")
                else:
                    print("enter a valid amount for transaction")
            elif trans=="quit":
                quit=input("press to quit  ")
                if quit=="yes":
                    print("quit")
                else:
                    print("choose any transaction please:")
        else:
            print("your password is not valid !Try again")
    else:
        print("your password is wrong")
else:
    print("Sorry, we dont have this language")
print("thank for using sbi")