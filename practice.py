#Write a program to print "Hello, World!"
print("Hello World")

#Take two numbers as input and print their sum.
a=int(input("enter first number : "))
b=int(input("enter second number : "))
sum=a+b
print(sum)

#Check if a number is even or odd.
aa=int(input("Enter number : "))
if aa%2==0:
    print("the number is even ")
else:
    print("the number is odd")

#Find the largest of three numbers.
a=78
b=87
n=98
list=[a,b,n]
largest=list[0]
for i in range(len(list)):
    if list[i]>largest:
        largest=list[i]
        print(largest)

