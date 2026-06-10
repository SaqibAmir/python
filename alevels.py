# # stings
# a="my name is saqib amir"
# print(a[1:2])
# # if else
# num =[1,3,55,66,88,76,55,332,354,]
# a=int(input("Enter the number to be searched: "))
# for x in num:
#     if x==a:
#       print("found")
#
# #while loop
# # Write a program to sum all the numbers between 1 to 100 using a while loop.
# t=0
# for m in range(0,100):
#      t=t+m
#
# print(t)
# Write a program to print all the even numbers between 1 to 100 using a while loop.
# Program to print all even numbers from 1 to 100 using while loop
#
# num = 1
#
# while num <= 100:
#     if num % 2 == 0:
#         print(num)
#     num += 1

#Write a program to prints all the characters except vowels (a, e, i, o, u) in a string
# name = "my name is saqib"
# vowels="aeiouAEIOU"
# m=0
# while m<len(name):
#     if name[m] not in vowels:
#         print(name[m],end="")
#     m+=1
# Write a program to find the sum of all the odd numbers between 1 to 100 using a
# i=1
# sum=0
# while i<=100:
#     if i%2 != 0:
#         sum=sum+i
#     i=i+1
# print(sum)
#12. Multiples of 5 till 50 (while).
# i=1
# while i<=10:
#     print("5 X ",i,"=",5*i)
#     i=i+1
#
# Sum of first n natural numbers.
# natural=int(input("Enter natural number: "))
# i=1
# sum=0
# while i<=natural:
#     sum=sum+i
#
#
#     i=i+1
# print(sum)
# 14. Factorial of n.
#  15. Multiplication table of n.
#  16. Keep asking numbers until 0. Print count and total.
#  17. Count digits in a number.
#  18. Print n down to 1 (while).
#  19. Sum of even numbers up to n.
#  20. Guessing game (secret = 15)
# e=int(input())
# fact=1
# i=1
# while i<=e:
#     fact*=i
#     i+=1
#
# print(fact)
# secret=15
# guess=int(input("enter your guess:"))
# attempts=0
# if guess==secret:
#     print("you guessed it right at ")
# else:
#    while guess != secret:
#        attempts=attempts+1
#
#        guess=int(input("enter your guess again and if you want to forfiet then enter 0 :"))
#        if guess == 0:
#            break
#        elif guess == secret:
#            print("you guessed it right at ",attempts,"attempts")
#        else:
#            print ("you guessed it wrong")
# Input 5 names. Print reverse.
# Input 10 integers + target. Print index or Not found (no break)
# Input 10 integers + target. Print frequency.
#Input 10 integers. Copy non-zeros
#Input 10 integers. Sum elements at even indexes.
# Input 10 integers. Count positives.
# list1=[]
# reverse=[]
# shuffle=4
# p=0
# for x in range (5):
#     names=input("enter your name")
#     list1.append(names)
# while p<=len(list1) and shuffle >=0:
#     reverse.append(list1[shuffle])
#     shuffle=shuffle-1
#     p+=1
# print(list1)
# # print(reverse)
# list1=[]
# v=0
# found=False
# for x in range (10):
#     a=int(input("please enter a number : "))
#     list1.append(a)
# b=int(input())
#
# while found == False :
#     if b == list1[v]:
#         print(v)
#         found=True
# def a ():
#     print("if you want to add number into list THEN PRESS 1 , If you want to delete then press 0 and if you want to quit then press 99")#     v=v+1
#     list1=[]
#     while True:
#
#         intp=int(input("Enter : 1 "
#                   "Remove : 0 "
#                   "Exit : 99 "
#                    "Show : 3 "))
#         if intp==1:
#             x=input("Enter what you want to add : ")
#             list1.append(x)
#         elif intp==0:
#             list1.pop()
#         elif intp==3:
#              print(list1)
#         else:
#              break
#

#my code was impressive
# it is should need little improvement
ff="saqib"
print(ff[0
      ])