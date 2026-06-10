                                                        # While loop

#question no.1 
#  Write a program to sum all the numbers between 1 to 100 using a while loop.
x=1
sum=0
while x<=100:
    sum=sum+x
    x=x+1
    

#question 2
# Write a program to print all the even numbers between 1 to 100 using a while loop
o=1
while o<=100:
    if o%2==0:
      print(o)
    o=o+1  

# question 3
# Write a program to check whether a number is prime or not.
x=int(input("input number"))
if x<=1:
   print("not a prime number")
elif x>1 and x%2==0:
   print("your number is prime number")
   


#question 3
#  Write a program to prints all the characters except vowels (a, e, i, o, u) in a string given by the user   
def cc(s):

   l=len(s)
   x=0
   while x<l:
      if s[x]!="a":
         if s[x]!="e":
            if s[x]!="i":
               if s[x]!="o":
                  if s[x]!="u":
                     print(s[x],end=" ")
    
             
   x=x+1
s=str(input("input a string"))  
# question 5
#  Write a program to find the sum of all the odd numbers between 1 to 100 using a while loop.
x=1
while x<=100:
   if not(x%2==0):
      print(x)
   x=x+1                                                  

                                                         
                                                         
                                                         
                     


