class BankAccount:
  def __init__(self, account_number, account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holdername=account_holder_name
    self.__account_balance=initial_balance
  def deposit(self, amount):
    if amount>0:
      self.__account_balance+=amount
      print("Deposit ₹ {}.New Balance:₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit number or insufficient amount.")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-=amount
      print("withdraw ₹{}.New balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("Account balance for {}(Account#{}): ₹{}".format(self.__account_holdername,self.__account_number,self.__account_balance))
account=BankAccount(account_number="12345678",account_holder_name="monisha",initial_balance=500.0)
account.display_balance()
account.deposit (500.0)
account.withdraw(100.0)
account.display_balance()
