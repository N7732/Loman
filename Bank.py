import datetime
x=datetime.datetime.now()
print(f"\n{x.strftime("%c")}    WELCOME IN OLIVO BANKING SYSTEM\n")
accounts={}#STORE CLIENT DETAILS
accs = {} #STRORE ACCOUNT DETAILS
N=[]
Withdrawlist=[]
loanlist=[]
loan_info={}#STORE LOAN DETAILS
class Bank:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.ssn=None
        self.client_saving=[]
    def create_account(self):
        ny=str(input("Enter you full name :"))
        Gny=ny.replace(" ","")
        NY=int(input("Enter you birth year:"))
        nyl=list(Gny)
        NYl=2025-NY
        bala=int(input("Enter amount great than 2000 in order to validate your account:"))
        self.balance=bala
        if self.balance<2000:#HERE HELP TO ENTER AMOUNT AT SECOND TIME
            print("\nPLEASE ENTER MORE THAN 2000 FOR ACTIVATING ACCOUNT")
            bala=int(input("SAVE again your initial amount more than 2000: "))
            if bala<2000:
                print("You failed to activate your account:")
            else:
                self.client_saving.append(bala)
                N.append(self.client_saving)
                cd=f"BK2025{len(nyl)}{NYl}1{nyl[1]}23"
                accounts["Name:"]=ny
                accounts["account_number"]=cd
                accounts["amount"]=self.client_saving
                accs[cd]=accounts
                self.owner=ny
                print("Creation of Account is successfull!")
                return f"Congultration Mr:{self.owner} You account number is:{cd} Total amount : {sum(accounts['amount'])}Rwf\n" 
        else:
            self.client_saving.append(bala)#DIRECTG TO ENTER AMOUNT MORE THAN 2000
            N.append(self.client_saving)
            cd=f"BK2025{len(nyl)}{NYl}1{nyl[2]}23"
            accounts["Name"]=ny
            accounts["account_number"]=cd
            accounts["amount"]=self.client_saving
            accs[cd]=accounts
            self.owner=ny
            print("Creation of Account is successfull!")
            return f"Congultration Mr:{self.owner} You account number is:{cd} Total amount : {sum(accounts['amount'])}Rwf" 
class verify(Bank):
    def __init__(self,owner,balance=0):
        super().__init__(owner,balance)
    def perform(self):
        opt = input("Enter your bank acount: ")
        found=False
        for x in accs.keys():
            if opt in x:
                print(f"{accounts['account_number']} This account is already exist in OLIVO BANKING SYSTEM The owner is {accounts["Name"]}")
                found=True
                break
        if not found:
            return"Invalid account\n"
class saving(Bank):
    def __init__(self,owner,deposited_amount,rate,balance=0):
        super().__init__(owner,balance)
        self.deposited_amount=deposited_amount
        self.rate=rate
    def deposited(self):
        found=False
        for x in accs.keys():
            if self.owner in x:
                interest=self.deposited_amount*self.rate 
                self.balance = self.balance + self.deposited_amount
                self.balance += interest
                print(f"Your are giong to save you maney at:{accounts['account_number']} owned by {accounts["Name"]}")
                if isinstance(accounts["amount"], list):
                   accounts["amount"].append(self.balance)
                   TOTAL_AMOUNT=(sum(accounts["amount"]))
                else:
                    accounts["amount"] = [accounts["amount"], self.balance]
                return f"Your new balance is {TOTAL_AMOUNT}Rwf"
        if not found:
            print("Invalid account")
class withdrow(saving):
    def __init__(self,owner,deposited_amount,rate,withdrow_balances,balance=0):
        super().__init__(owner,deposited_amount,rate,balance)
        self.withdrow_balances=withdrow_balances
    def withdow_balance(self):
         for x in accs:
            if self.owner in x:
                if sum(accounts["amount"]) > self.withdrow_balances:
                    if isinstance(accounts["amount"],list):
                       accounts["amount"].append(-self.withdrow_balances)
                       Withdrawlist.append(self.withdrow_balances)
                       return f"You withdrown {self.withdrow_balances}Rwf\nNew Balance:{sum(accounts['amount'])}Rwf\n"
                    else:
                        return("System error")
                else:
                    return f"No balance you have equal to {self.withdrow_balances}Rwf\n New balance is {sum(accounts['amount'])}Rwf\n"
class loan(saving):
    def __init__(self,owner,deposited_amount,rate,allowed_loan,profit_rate,balance=0):
        super().__init__(owner,deposited_amount,rate,balance)
        self.allowed_loan=allowed_loan
        self.profit_rate=profit_rate
    def L(self):
        if len(loanlist)<=2:
            w=sum(accounts["amount"])*3
            if w>self.allowed_loan:
                loanlist.append(self.allowed_loan)
                profit=self.allowed_loan*self.profit_rate
                loanlist.append(profit)
                total=profit+self.allowed_loan
                return f"You BORROWED:{self.allowed_loan}Rwf\nYou will return:{total} "
            else:
                return f"You have not enough balance"
        else:
            return f"Pay your loan first of all"
class returned_loan(loan):
    def __init__(self,owner,deposited_amount,rate,allowed_loan,balance=0):
        super().__init__(owner,deposited_amount,rate,allowed_loan,balance)
    def pay_loan(self):
        chose=int(input("You want to start to pay your loan\n1.Yes\n2.No"))
        if chose==1:
            account=str(input("Enter account again:"))
            if account==accounts["account_number"]:
                paying_amount=int(input("Enter amount you want to pay:"))
                loanlist.append(-paying_amount)
                if sum(loanlist)>=0:
                   return f"Amount remained as loan :{sum(loanlist)}"
                else:
                    if isinstance(accounts["amount"],list):
                        accounts["amount"].append(-sum(loanlist))
                        return f"You paid more than our loan remained amount goes into your saving account\nNow you new balance:{sum(accounts['amount'])}"
            else:
                return f"Your account Not valid"
class Admin:
    def __init__(self, password):
        self.password = password
    def check(self):
        set_password="2025S"
        choice=str(input("Enter password:"))
        if choice==set_password:
            for x,y in accounts.items():
                return f"Accounts information:\n{x,y}\n"
            else:
                print("Invalid password")
    def display_info(self):
        return f"Bank system accounts Now at {x.strftime("%X")}\n\n{accs}"
    def check_loan(self):
        for acc in accs:
            loan_info [acc['account_number']]=loanlist
            return f"\nLoan Tables\n{loan_info}"
    def remove_account(self):
        print("Your want to remove account?")
        chose=int(input("Enter your choice 1.Yes or 2.No"))
        if chose==1:
            account_number=str(input("Account number:"))
            for x in accs.keys():
                accs.pop(account_number)
                return f"account Remained in system:{accs}"
        if chose==2:
            return f"Ok"
        else:
            return"Invalid Option"
counter=0
while(True):
    def main():
        print("MAIN Menu:")
        print("A.Create Account in our system\nB.Check if you account exixt\nC.Saving\nD.Withdraw\nE.Administration\nF.Other service!\n")
        choice = str(input("Enter your choice: "))
        if choice=="A"or choice=="a":
            h=Bank("")
            print(h.create_account())
        elif choice=="B" or choice=="b":
            v=verify("")
            print(v.perform())
        elif choice=="c" or choice=="C":
            deposited_amount=int(input("Enter Amount you want to save:"))
            owner=str(input("Enter your account:"))
            rate=0.05
            t=saving(owner,deposited_amount,rate)
            z=saving(owner,deposited_amount,rate)
            print(t.deposited())
        elif choice=="D" or choice=="d":
            withdrow_balances=int(input("Enter amount you want to witdraw:"))
            owner=str(input("Enter Account you want to withdraw:"))
            if owner==accounts["account_number"]:
                rate=0.05
                Z=withdrow(owner,0,rate,withdrow_balances,0)
                print(Z.withdow_balance())
            else:
                return f"Account Not found! "
        elif choice=="E" or choice=="e":
            c=Admin(2025)
            print(c.check(),c.display_info(),c.check_loan(),c.remove_account())
        elif choice=="F" or choice=="f":
            print("1.LOAN\n2.Returned_loan\n")
            opti= int(input("Chose number to continue in above service:"))
            if opti==1:
                owner=str(input("Enter Account you want to borrow to:"))
                if owner==accounts["account_number"]:
                    w=sum(N)*4
                    print(f"Amount you allowed is equal :{w} \nAre you satisfied?\n1.YES\n2.NO")
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        allowed_loan=int(input("Enter Amount your want: "))
                        Y=loan(owner,0,0,allowed_loan,0.18,0)
                        print(Y.L())
                    elif choice==2:
                        print("Contact us or come to our administration")
                    else:
                        print("Invalid option")
                else:
                    return f"This account not found!"
            elif opti==2:
                owner=str(input("Enter your account:"))
                O=returned_loan(owner,0,0,0,0)
                print(O.pay_loan())
            else:
                print("Invalid Option")
        else:
            print("Invalid option")
    if __name__ == "__main__":
        main()
    counter +=1 



