import datetime
x=datetime.datetime.now()
print(f"\n{x.strftime("%c")}    WELCOME IN OLIVO BANKING SYSTEM\n")
class Bank:
    def __init__(self,account,owner,balance=0):
        self._account=account
        self.owner=owner
        self.balance=balance
        self._ssn=None
    @property
    def account(self):
        return "*******" + str(self._account)[-2:]
    def deposit(self):
        pass
        return f"Account Number :{self.account} owned by {self.owner} your initial balance is: {self.balance}\n"
class saving(Bank):
    def __init__(self,account,owner,deposited_amount,rate,balance=0):
        super().__init__(account,owner,balance)
        self.deposited_amount=deposited_amount
        self.rate=rate
    def deposited(self):
        interest=self.deposited_amount*self.rate 
        self.balance+=self.deposited_amount +interest
        return f"You deposited:{self.deposited_amount}Rwf and we must add profit:{interest}Rwf\nSo Your new balance is {self.balance} \n"
class withdrow(saving):
    def __init__(self,account,owner,deposited_amount,rate,withdrow_balances,balance=0):
        super().__init__(account,owner,deposited_amount,rate,balance)
        self.withdrow_balances=withdrow_balances
    def withdow_balance(self):
        self.deposited()
        if self.balance> self.withdrow_balances:
            self.balance-=self.withdrow_balances
            return f"You withdrown {self.withdrow_balances}Rwf you remained on account {self.balance}Rwf\n"
        else:
            return f"No balance you have equal to {self.withdrow_balances}Rwf you balance is {self.balance}Rwf\n"
class loan(saving):
    def __init__(self,account,owner,deposited_amount,allowed_loan,rate,balance=0):
        super().__init__(account,owner,deposited_amount,rate,balance)
        self.allowed_loan=allowed_loan
    def L(self):
        self.deposited()
        w=self.balance*4
        if w>self.allowed_loan:
            return f"You allowed loan equal:{w} you gotted:{self.allowed_loan}Rwf\n"
        else:
            return f"You have not enough balance"
class returned_loan(loan):
    def __init__(self,account,owner,deposited_amount,allowed_loan,rate,profit_rate,balance=0):
        super().__init__(account,owner,deposited_amount,allowed_loan,rate,balance)
        self.profit_rate=profit_rate
    def borrow(self):
        self.L()
        profit=self.allowed_loan*self.profit_rate
        total=self.allowed_loan+profit
        return f"You will return:{profit}Rwf then sum is {total}Rwf this you supposed to pay!\n"
h=Bank("BK1234RW17","N.Olivier",20000)
print(h.deposit())
t=saving("BK1234RW17","N.Olivier",30000,0.05,20000)
print(t.deposited())
Z=withdrow("wBK1234RW17","N.Olivier",30000,0.05,40000,20000)
print(Z.withdow_balance())
Y=loan("BK1234RW17","N.Olivier",30000,100000,0.05,20000)
print(Y.L())
O=returned_loan("BK1234RW17","N.Olivier",30000,100000,0.05,0.18,20000)
print(O.borrow())


