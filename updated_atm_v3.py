class Atm():
    pin=8008
    def __init__(self,name,passcode,balance=0):
        self.name=name
        self.balance=balance
        self.passcode=passcode
        print(f"{self.name} hyy good morning")
        
        for i in (1,2,3):
            
            if self.passcode==self.passcode:
                    print(f"{self.name} login complete")
                    return print(f"{self.name} thanks")
            else:
                print(f"{self.name} in valid credentials")
    def Add_amount(self,amount):
        self.amount=amount
        if amount>0:
            self.balance=self.balance+amount
            print(f"amount ${self.amount} added to {self.name}")
        else:
            print("transaction failed")
    def Withdraw_amount(self,amount):
        self.wamount=amount
        if self.balance>= amount:
            self.balance=self.balance-self.amount
            print(f"amount ${self.amount} is withdraw")
            print(f"current balance $ {self.balance}")
        else:
            print("transection failed")
    

        
user1=Atm('rohit',1234).Add_amount(500)
print(user1)
user1=Atm('rohit',1234).Withdraw_amount(400)
print(user1)
user1=Atm('rohit',1234).Add_amount(500)
print(user1)   
user1=Atm('rohit',1234).Withdraw_amount(700)
print(user1)
user1=Atm('rohit',1234).Add_amount(500)
print(user1)   
user1=Atm('rohit',1234).Withdraw_amount(700)
print(user1)