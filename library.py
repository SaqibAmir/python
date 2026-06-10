import self


class student:
    def __init__(self,name,age,roll,marks):
        self.name=name
        self.age=age
        self.roll=roll
        self.marks=marks

    def display(self):
        print(f"your name is {self.name}\n"
              f"your age is {self.age}\n"

              f"your roll is {self.roll}\n"
              f"your marks is {self.marks}\n")

class student:
    def __init__(self,name,age,rollno,marks):

        self.name=name
        self.age=age
        self.rollno=rollno
        self.marks=marks
        self.total=0
        for x in self.marks:
            self.total=self.total+x


    def  average(self):
        print("The Student ",self.name," with the roll number ",self.rollno ,"average is ",self.total/len(self.marks))


class rectangle:
    def __init__(self):
        self.x=int(input("enter the height of the rectangle : "))

        self.y=int(input("enter the width : "))

    def area(self):
        return self.x*self.y


class student1:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def result(self):
        if self.marks>40:
            print("Passed")
        elif self.marks<=40:
            print("Failed")
        else :
            print("Wrong Input")


class car:
    def start(self):
        self.isrunning=True

    def stop(self):
        self.isrunning=False

    def status(self):
        if self.isrunning:
            print("car is running")

        else:
            print("car is stopped")



class bankacc:

    def deposit(self):
        self.n=int(input(" Enter the deposit amount: "))
        self.bankbalance=0
        self.bankbalance=+self.n

    def withdraw(self):
        self.w=int(input(" Enter the withdraw amount: "))
        if self.w>self.bankbalance:
            print("You don't have enough money")
        elif self.w<=self.bankbalance:
            print("sucessfully withdrawn")
            self.bankbalance=self.bankbalance-self.w
        else:
            print("Please enter the correct amount")

    def balance(self):
        print(self.bankbalance)



class employee:
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company

    def display(self):
        return self.salary*12
    def comname(self):
        print(self.company)

class book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def l_or_s(self):
        if self.pages>300:
            print("Book is long")
        else :
            print("Book is short")



#Implement inheritance: Make a base class Animal and derived classes Dog and Cat with their own methods.
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class using super()
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks. It is a {self.breed}.")

# Another child class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent constructor
        self.color = color

    def meow(self):
        print(f"{self.name} meows. It is a {self.color} cat.")


# Create a class Calculator with static methods for add, subtract, multiply, and divide.
class Calculator():
    def __init__(self):
      self.f = int(input("Enter the first number: "))
      self.s = int(input("Enter the second number: "))
    def add(self):

        print(self.f+self.s)
    def subtract(self):
        print(self.f-self.s)

    def multiply(self):
        print(self.f*self.s)
    def divide(self):
        print(self.f/self.s)

