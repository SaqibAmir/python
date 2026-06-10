#OOPS
class student:
    def __init__(self):
        self.name=input("Enter Your name : ")
        self.roll=int(input("Enter your Roll number : "))
        self.age=int(input("Enter your age :"))
    def display(self):
        print(f"Student name is {self.name} who is {self.age} years older and its roll number is {self.roll}")

class engine:
    def start(self):
        self.engine_running=True
    def stop(self):
        self.engine_running=False
    def status(self):
        if self.engine_running:
            print("Vehical is running ")
        else:
            print("Vehical is stopped")

class Bankaccount:
    def __init__(self):
        self.name=input("Enter Your Name : ")
        self.num=int(input("Enter Your Account Number : "))
        self.total=0

    def withdraw(self):
        self.widthdraw=int(input("Enter the amount You want to Widthdraw : "))
        if self.widthdraw >self.total:
            print("Insuffificient Balance ")
        else:
            print("Sucessfully Widthdrawn")

    def deposit(self):
        self.deposit1=int(input("Please Enter The amount : "))
        self.total+=self.deposit1

    def status(self):
        print(f"{self.name} account [{self.num}] bank Balance is : {self.total}")

class calculater:
    def __init__(self):
        self.num1=int(input("Enter your First num : "))
        self.num2=int(input("Enter your second num : "))
    def add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def multiply(self):
        print(self.num1*self.num2)
    def divide(self):
        print(self.num1/self.num2)

class subscription:
    def __init__(self,subscripion_id,plan,total_paymnet):
        self.plan=plan
        self.total=total_paymnet
        self.sub=subscripion_id
    def subcribe(self):
        print(f"A person with the {self.sub} id has subcribed to {self.plan} with {self.total} payment ")
    def unsubscribe(self):
        print(f"A person with the {self.sub} id has unsubscribed to {self.plan}")
class premium_subcristion(subscription):
    def __init__(self, subscripion_id, plan, total_paymnet ,screens):
        self.screens=screens
        self.plan=plan
        self.total=total_paymnet
        self.sub=subscripion_id
        super().__init__(subscripion_id, plan, total_paymnet)


    def subcribe(self):
        print(f"A person with the {self.sub} id has subcribed to {self.plan} with {self.total} payment ")

    def unsubscribe(self):
        print(f"A person with the {self.sub} id has unsubscribed to {self.plan}")
    def max_sceens(self,screens):
        self.max_screns=screens

        print(f"maximum screens set to {self.max_screns}")
