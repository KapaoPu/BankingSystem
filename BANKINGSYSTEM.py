class user: # Parent class
    def __init__(self,name,age,date):
        self.name = name
        self.age = age
        self.date = date
    
    def showdata(self):
        print("ชื่อของคุณ : ",self.name)
        print("อายุของคุณ : ",self.age)
        print("วันเกิดของคุณ : ",self.date)

class bank(user):
    def __init__(self,name,age,date):
        super().__init__(name,age,date)
        self.balance = 0
# การใช้ self ทำให้ ฝังชั้นอื่นใน class สามารถนำข้อมูลไปใช้ได้ด้วย
    def deposit(self,amount):
        self.amount = amount
        if self.amount <0 :
            print("ไม่สามารถ ฝากเงินติดลบได้")
        else:
            self.balance += self.amount
            print("เงินภายในบัญชีตอนนี้",self.balance)
    
    def withdraw(self,amountwithdraw):
        self.amountwithdraw = amountwithdraw
        if self.amountwithdraw >self.balance:
            print("ไม่สามารถถอนเงินมากกว่าเงินในบัญชี้ได้")
        else:
            self.balance -= self.amountwithdraw 
            print("เงินภายในบัญชีตอนนี้",self.balance)

    def view_balance(self):
        print("ข้อมูลของคุณ")
        self.showdata()
        print("เงินภายในบัญชีของคุณ : ",self.balance)

# test = bank("yok",17,"5 august 2548")
# test.deposit(600)
# test.withdraw(200)
# test.view_balance()

account = bank(input("ใส่ชื่อของคุณ : "),int(input("ใส่อายุของคุณ : ")),input("ใส่วันเกิดของคุณ : "))
while True:
    x = input("คุณต้องการฝากเงินหรือถอนเงินหรือดูยอดเงินในบัญชี : ฝาก / ถอน / ดูยอด : ")
    if x== "-1":
        break
    if x == "ฝาก":
        account.deposit(int(input("ใส่จำนวนเงินที่ต้องการฝาก : ")))
    elif x == "ถอน":
        account.withdraw(int(input("ใส่จำนวนเงินที่ต้องการถอน : ")))
    else:
        account.view_balance()