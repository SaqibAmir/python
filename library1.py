# #Write a class Car that has a constructor to initialize brand, model, and year. Also, add a method display() that prints all the car details.
# from library import student
#
#
# class Car :
#     def __init__(self, brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display(self):
#         print(f"The car Brand is {self.brand}")
#         print(f"The car Model is {self.model}")
#         print(f"The car Year is {self.year}")
#
# #Create a base class Animal with method sound(), and override it in Dog and Cat subclasses with appropriate sounds.
#
# class Animal:
#     def sound(self):
#         print("Animal make sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog sound")
#
# class Cat(Animal):
#     def sound(self):
#         print("Cat sound")
#
# #Create a class Employee that has a class variable company_name and an instance variable employee_name. Print both using an object.
# class Employee(Animal):
#     def __init__(self,company,employee):
#         self.company = company
#         self.employee = employee
#     def display(self):
#         print(f"The employee is {self.employee}")
#         print(f"The employee is {self.company}")
#
# #Create a class Vehicle and subclass Truck. Use super() to call the parent constructor.
# class Vehicle:
#     def __init__(self,wheels,engine):
#         self.wheels = wheels
#         self.engine = engine
#
#         print("which vehicle is this")
# class truck(Vehicle):
#     def __init__(self,wheels,engine,tons):
#         super().__init__(engine,wheels)
#         self.tons = tons
#         print(f"the truck is created with {self.tons} tons and {self.wheels} wheels")
#
# #Create a class BankAccount with deposit and withdraw methods and a balance attribute. Initialize it with a starting balance.
# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#         print("the bank account is created")
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"The balance is {self.balance}")
#     def withdraw(self,amount):
#         if self.balance >= amount:
#            self.balance -= amount
#            print(f"The balance is {self.balance}")
#         else :
#             print("You don't have enough money")
#
# #Use a class variable to keep track of how many objects of a class Book have been created.
#
# class Book:
#     count = 0  # class variable to track number of objects
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.count += 1  # increment class variable when a new object is created
#
#
#
# #Create a class Student with private attributes __marks and __name. Use getter and setter methods to access them.
# class Student1:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def ngetter(self):
#         return self.name
#     def mgetter(self):
#         return self.marks
#     def nsetter(self, value):
#         self.marks = value
#         return self.ngetter()
#     def msetter(self, value):
#         self.marks = value
#         return self.mgetter()
#
# #Create a class Shape with a method area(). Inherit it in Rectangle and Triangle, override the area() method in each.
#
# class shape:
#     def area(self):
#         print("The shape is area")
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#
#
# class triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def area(self):
#
#         return (1/2*self.a*self.b)*2
#
# # Create a class MathTools with:
# #
# # A static method add(a, b)
# #
# # A class method info() that prints a class-level message
#
# class MathTools:
#     # Static method: does not access class or instance data
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     # Class method: accesses class-level data or behavior
#     @classmethod
#     def info(cls):
#         print("This class provides basic math tools like addition.")
#
#
#
# #Create an abstract class Device with an abstract method turn_on(). Inherit it in Laptop and Mobile classes and implement the method.
# from abc import ABC, abstractmethod
# class device(ABC):
#     def turn_on(self):
#          pass
#
#
#
# class laptop(device):
#     def turn_on(self):
#
#        print("Laptop is now ON 💻")
# class mobile(device):
#     def turn_on(self):
#             print("Turned on the device")
#
#
#
#
# #Implement polymorphism: Create a method make_sound() in classes Cat, Dog, and Cow with different outputs. Call them using a single loop.
# class animals:
#     def malesound(self):
#         print("the animal make sound")
#
# class dog :
#     def makesound(self):
#         print("the dog make sound")
#
# class cat:
#     def makesound(self):
#         print("the cat make sound")
# class cow:
#     def makesound(self):
#         print("the cow make sound")
#
#
# #Create a class Flight with class variable total_flights. Each time a flight is created, increment the count.
# class Flight:
#     total_flights=0
#     def flights(self):
#         print("flight has been created")
#         self.total_flights+=1
#
#
# #Create a class Smartphone and add Battery class to it using composition. Add method battery_status() that prints charge percentage.
#
#
# class Battery:
#     def __init__(self, percentage):
#         self.percentage = percentage
#
#     def get_charge(self):
#         return f"Battery at {self.percentage}% charge."
#
#
# class Smartphone:
#     def __init__(self, model, battery_percentage):
#         self.model = model
#         self.battery = Battery(battery_percentage)  # Composition
#
#     def battery_status(self):
#         print(self.battery.get_charge())
#
#
#
#
# #Write a class Temperature with methods to convert Celsius to Fahrenheit and vice versa.
# class Temprature:
#     def __init__(self, celcius):
#         self.celcius = celcius
#
#     def converter(self):
#         a=self.celcius*9/5+32
#         print(a)
#
# #Create a Library class that contains a list of Book objects (composition). Add methods to add and display books.
# class library:
#     list_books=[]
#     def books(self,tiltle):
#         self.tiltle = tiltle
#         self.list_books.append(tiltle)
#     def display(self):
#         for book in self.list_books:
#             print(book)
#
# #Create a class Employee and a subclass Manager. Add a method work() that’s overridden in both.
# class employee:
#     def work(self):
#         print("employee working")
# class Manager(employee):
#     def work(self):
#         print("Manager working")
#
# #Create a class Rectangle with a method area(). Create a subclass Square and override area().
# class  rectangle:
#     def area(x,y):
#
#         return x*y
#
# class square(rectangle):
#     def area(x,y):
#
#         return x*y
#
#
#
# #Create a class Author and a class Book. Use composition to store an Author object in the Book class.
# class author:
#     def __init__(self,x,n):
#         self.name=x
#         self.nationality=n
#     def displayinfo():
#
#             print(f"the author's name is {self.name} and nationality is {self.nationality}")
#
# class book:
#     def __init__(self,name1,pages,author):
#         self.name1 = name1
#         self.pages = pages
#         self.author = author
#     def display(self):
#         print (f"the book is created with name {self.name1} author {author} with  {self.pages}pages ")
#         self.author.displayinfo()
#
#
# #Create a class School with a list of Student objects using composition. Add methods to add students and display them.
# # Student class
# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
#
#     def display_info(self):
#         print(f"Student Name: {self.name}, Roll No: {self.roll_number}")
#
# # School class using composition
# class School:
#     def __init__(self, name):
#         self.name = name
#         self.students = []  # List to store Student objects
#
#     def add_student(self, student):
#         self.students.append(student)
#         print(f"✅ {student.name} has been added to {self.name}.")
#
#     def display_students(self):
#         if not self.students:
#             print("🚫 No students enrolled yet.")
#         else:
#             print(f"📋 Student list for {self.name}:")
#             for student in self.students:
#                 student.display_info()
#
#
#
# #Demonstrate polymorphism with a method start_engine() in classes Bike, Car, and Truck. Call them in a loop.
#
#
# # Class definitions with the same method name
# class Bike:
#     def start_engine(self):
#         print("🏍️ Bike engine started with a kick!")
#
# class Car:
#     def start_engine(self):
#         print("🚗 Car engine started with a button!")
#
# class Truck:
#     def start_engine(self):
#         print("🚚 Truck engine started with a key and heavy ignition!")
#
# # Polymorphic behavior: objects of different types in one list
# vehicles = [Bike(), Car(), Truck()]
#
# # Loop through each vehicle and call the same method
# for vehicle in vehicles:
#     vehicle.start_engine()
#
# #Use super() to call the parent constructor in a class hierarchy of Device -> Phone.
#
# class device:
#     def __init__(self,model):
#         self.model = model
# class phone(device):
#     def __init__(self,model,number):
#         super().__init__(model)
#         self.number =number
#         print(f"the phine with number is {self.number}, and model is {model} is started.")


#Design a small OOP system for an online course platform with classes like User, Course, Instructor, and Student.
class user:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"{self.name} is joining the course")
class Instructor(user):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.name=name
        self.email=email
        self.expertise = expertise

    def display_info(self):
        super().display_info()
        print(f"📘 Expertise: {self.expertise}")

class Students:
    def __init__(self,name,age,roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def display_info(self):
        print(f"the student name is {self.name}"
              f"and age is {self.age}"
              f"and roll number is {self.roll_number}")





class Course(Students):
    def __init__(self,course,name1,age,roll_number):
        self.course = course
        super().__init__(name1,age,roll_number)
        self.courses=[]

    def add_course(self):
        self.courses.append(self.course)


    def display_info(self):
        print(f"the student {self.name} is joining {self.course}")


a = user("saqib", "saqibkbty741@gmail.com")
a.display_info()
b = Students("saqib", 16, 8899)
b.display_info()
c = Course("python Course", "saqib", 66, 9900)
c.add_course()
c.display_info()
