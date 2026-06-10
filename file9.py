# Create a program.
# 1)	This contains 5 subroutines.
# a)	Input 5 numbers in an array
# b)	Linear Search
# c)	Binary Search
# d)	Bubble Sort
# e)	Insertion Sort
# 2)	In main program ask the user to enter 5 numbers
# 3)	Ask him to choose 1, either search or sort
# 4)	Then give him a choice to choose either of the searching or sorting algorithm
# 5)	Give the output
# 6)	Incase of binary search, do sort the array 1st
# 7)	Keep repeating, and keep giving the choice until he presses 3. That means END.


def binary_search(arr,tar):
    upper=len(arr)-1
    lower=0
    found=False
    while found==False and lower<=upper:
        index=int((lower+upper)/2)
        if arr[index]==tar:
            found=True
        elif arr[index]<tar:
            lower=index+1
        elif arr[index]>tar:
            upper=index-1
    if found==True:
        print(f"Target {tar} found at {index}")
    else:
        print("Not Found")
def linear_search (arr,tar):
    found=False
    for x in range(len(arr)):
        if arr[x]==tar:
            found=True
    if found == True:
        print(f"Target {tar} found at {x}")
    else:
        print("Not Found")

def bubble_sort(arr):
    swapped=True
    while swapped==True :
        swapped = False
        for x in range(0,len(arr)-1):
            if arr[x]>arr[x+1]:
                temp=arr[x]
                arr[x]=arr[x+1]
                arr[x+1]=temp
                swapped=True
    return arr

def array_maker(arr):
    for x in range(5):
        n=int(input("enter 5 numbers : "))
        arr.append(n)
    print(f"Your list is : {arr}")
arr=[]
array_maker(arr)
while True:
   n=int(input("now You have three choices \n1. To sort\n2. To search \n3. To exit "))
   if n==1:
       a=bubble_sort(arr)
       print(f"Your sorted list is {a}")
   elif n==2:
       m=int(input("1. linear search\n2. Binary search"))
       if m==1:
           tar=int(input("What Your target"))
           linear_search(arr,tar)
       elif m==2:
           c=bubble_sort(arr)
           tar = int(input("What Your target"))
           binary_search(c,tar)
   elif n==3:
       print("thank You")
       break