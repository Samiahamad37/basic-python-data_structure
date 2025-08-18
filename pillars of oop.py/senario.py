class Bank:
    def __init__(self, name,amount):
        self.name=name
        self.amount=amount
    
    def deposit(self, deposited_amount):
        if 0<deposited_amount:
            self.amount +=deposited_amount
            print(f"{deposited_amount}Tsh is added {self.name}, the new balance is {self.amount}")
            
        else:
            print('no amount deposited')
        
    def withdraw(self, removed_amount):
        if removed_amount >0 <=self.amount:
            self.amount -=removed_amount
            print(f"{removed_amount}Tsh is removed from {self.name} the remaining balance is {self.amount}")
            
        else:
            print(f"u dont have enough balance")
    
    def checkbalance(self):
        print(f"your balance is {self.amount}")
  
  
  
        
obj1=Bank("NMB", 70000)
obj1.deposit(30000)
obj1.withdraw(20000)
obj1.checkbalance()