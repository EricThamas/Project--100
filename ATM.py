class ATM:
    def __init__(self,ATMcard,pinNumber):
        self.ATMcard=ATMcard
        self.pinNumber=pinNumber
    def Balance(self):
        print("User Balance is 5000$")
    def BankEnquiry(self,amount):
        new_amount=5000-amount
        print("You Have Withdrawn"+ str (amount)+"Remaining Balance is"+ str(new_amount))
def setup():
    cardNumber=input("insert your cardNumber ")
    pinNumber=input("insert your pinnumber ")
    new_user=ATM(cardNumber,pinNumber)
    print("Which activity you want to do")
    print("1.Balance 2.Withdraw" )
    activity = int(input("Enter the activity number"))
    if(activity==1):
        new_user.Balance()
    elif(activity==2):
        amount=int(input("Enter the amount to withdraw"))
        new_user.BankEnquiry(amount)
    else:print("Enter the Valid amount number")
setup()                 

        

