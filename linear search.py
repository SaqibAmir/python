# #Write a program to perform linear search on a list of integers to find a target number.
# a=[12,33,56,7,7,11,4,6,64,32,]
# for x in a:
#     if x==11:
#         print("found")
#
# #Write a program that checks if a given name is in a list of student names using linear search.
# student_list=["saqib","muneeb","haseeb","ahmad"]
# for x in student_list:
#     if x=="saqib":
#         print("found")
#
# #Write a program to search for a specific character in a string using linear search.
# a='saqib is a pro cricketer'
# for x in a:
#     if x =="b":
#         print("found")
#
#
#
# #Search for an item in a list and print its index (or -1 if not found).
# def linear_search(lst, target):
#     for index in range(len(lst)):
#         if lst[index] == target:
#             return index
#     return -1
#
# # Example usage
# numbers = [10, 20, 30, 40, 50]
# item = int(input("Enter the number to search: "))
#
# result = linear_search(numbers, item)
#
# if result != -1:
#     print(f"✅ Item found at index {result}")
# else:
#     print("❌ Item not found (returned -1)")
#
# #Search through a list of 10 numbers and print "Found" or "Not Found".
# def linear_search1(list1, input):
#     found = False
#     for index in range(len(list1)):
#         if list1[index] == input:
#             found=True
#             return found
#
#     return found
# c=[12,44,775,3,2,4,5,6,99,77]
# n=int(input("Enter the number to search: "))
# result = linear_search1(c,n)
# if result ==True:
#     print("founded")
# else:
#     print("not found")
#
#
# #Search for multiple occurrences of a number in a list and return all their indexes.
# def find_all_occurrences(lst, target):
#     indexes = []
#     for i in range(len(lst)):
#         if lst[i] == target:
#             indexes.append(i)
#     return indexes
#
# # Example usage
# numbers = [4, 7, 2, 7, 9, 7, 1]
# item = int(input("Enter the number to search: "))
#
# result = find_all_occurrences(numbers, item)
#
# if result:
#     print(f"✅ Found at indexes: {result}")
# else:
#     print("❌ Item not found in the list.")
#
#
# #Search in a list of dictionaries (e.g., students with {"name": "Ali", "roll": 101}) for a specific name.
#
# def search_student_by_name(students, target_name):
#     for student in students:
#         if student["name"].lower() == target_name.lower():
#             return student
#     return None
#
#
# students=[
#     {"name" : "saqib", "roll" : 8899},
#     {"name" : "haseeb", "roll" : 889},
#     {"name" : "muneeb", "roll" : 99},
#
# ]
# search_name=str(input("what name do you want to search?"))
#
# a=search_student_by_name(students, search_name)
# print(a)
#
#
# #Write a function linear_search(arr, target) that returns True or False based on presence of target.
# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return True
#     return False
# a=(linear_search([1,2,3,4,5,6,7,8,9],3))
# print(a)
#
# #Search for a student's marks by their name in a list of tuples like [("Ali", 85), ("Sara", 90)].
# def linear_search(tuple,target):
#     n="False"
#     for name , mark in tuple:
#         if name.lower()==target.lower():
#             return mark
#
#     return n
#
# a=[("Ali",85),("sara",90),("muneeb",12)]
# b=str(input("which person marks you want to search : "))
# c=(linear_search(a,b))
# print(c)
#
#
# #Search for a substring in a sentence using a linear scan.
# def scan (str1,sen):
#     if str1 in sen:
#         return True
#     else:
#         return False
#
# a="im 16 years old"
# b="old"
# a=scan(b,a)
# print(a)
#
#
# #Implement linear search on a 2D list (matrix) and return the position (row, col) of the target element.
# #Modify linear search to find the first even number in a list.
# def matrix_search(matrix):
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if matrix[row][col]%2==0:
#                 return (row,col)
#
#
# a=([1,2,4,53,2,4,43,4],
#    [2,3,55,4,32,22,2,7])
#
# c=matrix_search(a)
# print(c)
#
# #Count how many times a target number appears in a list using linear search.
#
# def matrix_search(matrix,target):
#     count = 0
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if matrix[row][col]==target:
#                 count+=1
#
#
# a=([1,2,4,53,2,4,43,4],
#    [2,3,55,4,32,22,2,7])
# b=int(input("Enter the number : "))
# c=matrix_search(a,b)
# print(c)
#
#
# #Search for the smallest/largest number in a list using linear iteration.
# def linear_iteration(list1):
#     largest=0
#     smallest=10
#     for x in range(len(list1)):
#         if list1[x] > largest:
#             largest=list1[x]
#
#     for x in range(len(list1)):
#         if list1[x] < smallest:
#             smallest=list1[x]
#
#     return f"the smallest is {smallest} and largest is {largest}"
#
# a=[10,3,5,54,33,3,56,6,75,5,5,556,5543,7]
# a=linear_iteration(a)
# print(a)

#////Build a menu-driven program where the user enters a list and performs multiple linear search queries on it.

# #Write a program to perform linear search on a list of integers to find a target number.
# a=[11,22,33,56,7865,33,87,32]
# for i in a:
#     if i == 56:
#         print("found 56")
#  #Write a program that checks if a given name is in a list of student names using linear search.
# student_list=["saqib","muneeb","haseeb","ahmad"]
# for i in student_list:
#     if i == "saqib":
#         print("found saqib")
# #Write a program to search for a specific character in a string using linear search.
# a='saqib is a pro cricketer'
# if "b" in a:
#     print("found saqib")
# #Search for an item in a list and print its index (or -1 if not found).
# def list_scan(list1,target):
#     for x in range(len(list1)):
#         if list1[x] == target:
#             print("found target at index ",x)
#             return
#         else:
#             print("not found target ")
#
# student_list=["saqib","muneeb","haseeb","ahmad"]
# a=list_scan(student_list,"saqib")
# print(a)
# # #Search through a list of 10 numbers and print "Found" or "Not Found".
#
# def target_scan(lit1,target):
#     for x in lit1:
#         if x == target:
#             return "Found"
#     return "Not Found"
# lit1=[21,23,34,46,434,31,421,53435,13,13]
# target=int(input("enter target number"))
# a=target_scan(lit1,target)
# print(a)

##Search for multiple occurrences of a number in a list and return all their indexes.
# def occurrence_scan(list1,target):
#     for x in range(len(list1)):
#         if list1[x] == target:
#             print("found target at index ",x)
#
#     return
# lit1=[21,23,34,46,434,31,421,53435,13,13]
# target=int(input("enter target number"))
# a=occurrence_scan(lit1,target)
##Search in a list of dictionaries (e.g., students with {"name": "Ali", "roll": 101}) for a specific name.
# def dict_search(a):
#     for x in a:
#       if "saqib" == x ["name"]:
#          print("found")
#
# b=[{"name" : "saqib", "roll" : 8899},
#  {"name" : "haseeb", "roll" : 889},
#  {"name" : "muneeb", "roll" : 99},
#
# ]
# dict_search(b)
##Search for a student's marks by their name in a list of tuples like [("Ali", 85), ("Sara", 90)].
# def tuple_search(tuple1,target):
#     for name,number in tuple1:
#         if name.lower() == target.lower():
#             print(number)
#
# li=  [("Ali",85),("sara",90),("muneeb",12)
#       ]
# n=(input("Enter the name to be searched: "))
# tuple_search(li,n)
#Implement linear search on a 2D list (matrix) and return the position (row, col) of the target element.
# #Modify linear search to find the first even number in a list
# def matrix_scan(mat,target):
#     for x in range(len(mat)):
#         for y in range(len(mat[x])):
#             if mat[x][y] == target:
#                 return (f"found at column {mat[x][y]}")
#     return -1
# mat1=([1,2,4,53,2,4,43,4],
#    [2,3,55,4,32,22,2,7])
# a=matrix_scan(mat1,2)
# print(a)
##Modify linear search to find the first even number in a list.
# def matrix_scan(mat,target):
#     for x in range(len(mat)):
#         for y in range(len(mat[x])):
#             if mat[x][y] %2==0:
#                 return (f"the even number {mat[x][y]} found at position {x},{y}")
#     return -1
# mat1=([1,2,4,53,2,4,43,4],
#    [2,3,55,4,32,22,2,7])
# a=matrix_scan(mat1,2)
# print(a)
##Count how many times a target number appears in a list using linear search.
# def count_tar(mat1,target):
#      count=0
#      for i in range(len(mat1)):
#          for j in range(len(mat1[i])):
#              if mat1[i][j] == target:
#                  count+=1
#      return count
# mat1=([1,2,4,53,2,4,43,4],
#     [2,3,55,4,32,22,2,7])
# a=count_tar(mat1,2)
# print(a)
#Search for the smallest/largest number in a list using linear iteration.
# def mat_scan(mat1):
#     largest=0
#     smallest=2
#     for x in range(len(mat1)):
#         for y in range(len(mat1[x])):
#             if mat1[x][y]>largest:
#                 largest=mat1[x][y]
#     for x in range(len(mat1)):
#         for y in range(len(mat1[x])):
#             if mat1[x][y]<smallest:
#                 smallest=mat1[x][y]
#
#     print(f"the largest is {largest} and the smallest is {smallest}")
# mat1=([1,2,4,53,2,4,43,4],
#      [2,3,55,4,32,22,2,7])
# mat_scan(mat1)
#Build a menu-driven program where the user enters a list and performs multiple linear search queries on it.
# def occurrence_scan(list1,target):
#     for x in range(len(list1)):
#         if list1[x] == target:
#             print("found target at index ",x)
#
#     return
# def even_scan(mat):
#     lis4=[]
#     for x in range(len(mat)):
#
#             if mat[x] %2==0:
#                 lis4.append(mat[x])
#
#     return (f"the even number are {lis4}")
# def mat_scan(mat1):
#     largest=0
#     smallest=2
#     for x in range(len(mat1)):
#
#             if mat1[x]>largest:
#                 largest=mat1[x]
#     for x in range(len(mat1)):
#
#             if mat1[x]<smallest:
#                 smallest=mat1[x]
#
#     print(f"the largest is {largest} and the smallest is {smallest}")
# print("Now you will enter the content of the list")
# print("Ready")
# list1=[]
# while True:
#     n=int(input("if you are ready then input 1 if you want to stop then enter 0 : "))
#     if n!=0:
#         list1.append(int(input("input any number : ")))
#     else:
#         break
# print(f"your list is {list1}")
#
# while True:
#    a=int(input("1: largest and smallest \n2: Even numbers \n3: target indexes \nWhat do you want to do? \nEnter 0 to exit :"))
#    if a==1:
#        mat_scan(list1)
#    elif a==2:
#        o=even_scan(list1)
#        print(o)
#    elif a==3:
#        a=int(input("Enter your target : "))
#        occurrence_scan(list1,a)
#    else:
#        break

# while linear search
# z=[23,54,687,4331,4324,6,53,86,974,3]
# i=0
# found=False
# m=int(input("Enter the index of the element you want to find: "))
# while found==False and i<len(z):
#     if z[i]==m:
#         found=True
#     else:
#         i=i+1
# if found==True:
#     print("Element found at index",i)
# else:
#     print("Element not found")
def find(list1):
    large=0
    small=1
    for  x in list1:
        if x>large:
            large=x
        if x<small:
            small=x
    print(f"Large value : {large}")
    print(f"Small value : {small}")
a=[1,3,55,7,5,4,3,23,33,43,0,3]
find(a)