class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    
    def checkbalance(self):
        print("Your Balance is $50000")
    
    def withdrawl(self,amount):
        new_amount=50000-amount
        print-("You have withdrawn"+str(amount)+"Your remaining balance is"+str(new_amount))

def main():
    card_number=input("insert your card number")
    pin_number=input("enter your pin number")
    new_user=Atm(card_number,pin_number)
    print("choose your activity")
    print("1.balance enquiry 2.withdrawl")
    activity=int(input("enter activity number"))
    if(activity==1):
        new_user.checkbalance()
    elif(activity==2):
        amount=int(input("enter the amount"))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ =="__main__":
    main()