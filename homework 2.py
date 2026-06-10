                                                            #For Loop


#question no.1
# Write a program to sum all the numbers between 1 to 100 using a for loop. 
sum=0
for x in range(1,100):
   sum=sum+x


# Write a program to print all the even numbers between 1 to 100 using a for loop. 
for x in range(0,100,2):
   print(x)

# Write a program to check whether a number is prime or not using for loop
num=65
if num<=1 and not num%2==0:
   print("non-prime number")
else:
   print("prime number")   


#Write a program to prints all the characters except vowels (a, e, i, o, u) in a string given by the user.   
a=str(input("input anything you want :"))
b=len(a)
for c in a:
   if c!="a"and c!="e"and c!="i"and c!="o"and c!="u":
    print(c,end=" ")
   

# Write a program to find the sum of all the odd numbers between 1 to 100 using a for loop.
sum=0
for x in range(1,100,2):
   sum=sum+x

print(sum)   