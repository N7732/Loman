import datetime
x=datetime.datetime.now()
print(f"\n{x.strftime("%c")}    WELCOME IN OLIVO BANKING SYSTEM\n")
print("MAIN Menu:")
print("A.Create Account in our system\nB.Check if you account exixt\nC.Saving\nD.Withdraw\nE.Administration\n")

accounts={}
accs = []
choice = str(input("Enter your choice: "))
class Bank:
    def __init__(self,owner,choice,balance=0):
        self._account=[]
        self._owner=owner
        self.choice=choice
        self.balance=balance
        self._ssn=None
    def create_account(self):
        if choice=="A"or choice=="a":
            N=[]
            ny=str(input("Enter you full name :"))
            Gny=ny.replace(" ","")
            NY=int(input("Enter you birth year:"))
            nyl=list(Gny)
            NYl=2025-NY
            bala=int(input("Enter amount great than 2000 in order to validate your account:"))
            self.balance=bala
            if self.balance<2000:
                print("\nPLEASE ENTER MORE THAN 2000 FOR ACTIVATING ACCOUNT")
                bala=int(input("SAVE again your initial amount more than 2000: "))
                if bala<2000:
                    print("You failed to activate your account:")
                else:
                    N.append(bala)
                    cd=f"BK2025{len(nyl)}{NYl}1{nyl[2]}23"
                    accounts["Name:"]=ny
                    accounts["account_number"]=cd
                    accounts["amount"]=N
                    self._account.append(accounts)
                    accs.append(accounts)
                    self.owner=ny
                    print("Creation of Account is successfull!")
                    return f"Congultration Mr:{self.owner} You account number is:{cd} make it secure{self._account}\n" 
            else:
                N.append(bala)
                cd=f"BK2025{len(nyl)}{NYl}1{nyl[2]}23"
                accounts["Name"]=ny
                accounts["account_number"]=cd
                accounts["amount"]=N
                self._account.append(accounts)
                accs.append(accounts)
                self._owner=ny
                print("Creation of Account is successfull!")
                return f"Congultration Mr:{self._owner} You account number is:{cd} make it secure{self._account}\n"
        elif choice=="B" or choice=="b":
            opt = input("Enter your bank acount: ")
            found=False
            for acc in accs:
                if acc["account_number"] == opt:
                    print(f"{acc['account_number']} This account is already exist in OLIVO BANKING SYSTEM The owner is {acc["Name"]}")
                    found=True
                    break
                if not found:
                    print("Invalid account")    

                else:
                    print("\nYou Entered invalid choice\n")
counter = 0
while counter:
    bank = Bank("w",2000)
    result = bank.create_account()
    if result:
        print(result)
    counter +=1 
h=Bank(0,2000)
print(h.create_account())  

#SAMPLE 

class ClassB:
    def activity_b(self):
        print("You are now performing an activity from Class B.")

    def extra_activity_b(self):
        print("Extra activity from Class B!")

class ClassA:
    def __init__(self):
        # Create an instance of ClassB inside ClassA
        self.class_b = ClassB()

    def activity_a(self):
        print("You are now performing an activity from Class A.")
        
        # Call a method from ClassB inside ClassA
        print("Now calling an activity from Class B inside Class A...")
        self.class_b.extra_activity_b()

def main():
    print("Choose an option:")
    print("A - Perform activities from Class A")
    print("B - Perform activities from Class B")
    
    choice = input("Enter your choice (A/B): ").strip().upper()

    if choice == 'A':
        a = ClassA()
        a.activity_a()
    elif choice == 'B':
        b = ClassB()
        b.activity_b()
    else:
        print("Invalid choice. Please enter A or B.")

if __name__ == "__main__":
    main()
counter = 0
while counter:
    bank = Bank(2000)
    result = bank.create_account()
    if result:
        print(result)
    counter +=1    

print("a")
d=Admin("AdminUser", "AdminRole", "D") 
print(d.welcome_admn())       

@property
def account(self):
        return "*******" + str(self._account)[-2:]
def deposit(self):
        self.create_account()
        return f"Account Number :{self._create_account()} owned by {self.owner} your initial balance is: {self.balance}\n"