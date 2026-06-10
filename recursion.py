# def rec(n):
#     if n==0:
#         return
#     print(n)
#     return rec(n-1)
# rec(6)
# sum=0
# def factorial(n):
#     global sum
#     if n==1 or n==0:
#         return 1
#     print(f"Factorial {n} * {n - 1} = ", n * n - 1)
#     return  n*factorial(n-1)
#
# factorial(9)
# print(sum)
# car=["buggati","cultus","civic","lamborghini","landcruser"]
# def list1(n,index=0):
#     if index ==len(n):
#         return
#     print(n[index])
#     index=index+1
#     return list1(n,index)
# list1(car)
# def search(target,n,index=0):
#     if index==len(n):
#         return False
#     if target==n[index]:
#         return True
#     index+=1
#     return search(target,n,index)
# a =search("cultus",car)
# print(a)

# large=0
# small=9999
# def large_smalls(n,index=0):
#     global large
#     global small
#
#     if index==len(n):
#         return
#     if n[index]>large:
#         large=n[index]
#     if n[index]<small:
#         small=n[index]
#     index=index+1
#     return large_smalls(n,index)
# large_smalls(list2)
# print(large,small)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [2,5,2]
# ]
# def mat_search(n,target,row=0,co=0):
#     if row==len(n):
#         print("not found")
#         return
#     if co==len(n[row]):
#         return mat_search(n,target, row+1, 0)
#     if n[row][co]==target:
#         print(row,co)
#         return
#     return mat_search(n,target, row, co+1)
# mat_search(matrix,9)
# def binary(array,target,low,high):
#     if high>=low:
#         mid=int(low+high/2)
#         if array[mid]==target:
#             return mid
#         elif array[mid]>target:
#             return binary(array, target, low, mid-1)
#         elif array[mid]<target:
#             return binary(array, target, mid+1, high)
#     else:
#          return -1

# a=binary(list2,980,0,len(list2)-1)
# if a==-1:
#     print("not found")
# else:
#     print(a)
list2=[34,86,8987,896,96,98,765,980]
def bubble(arr,index,lenght):
    if lenght==1:
        return arr
    if index==lenght-1:
        return bubble(arr, 0, lenght-1)
    if arr[index]>arr[index+1]:
        temp=arr[index]
        arr[index]=arr[index+1]
        arr[index+1]=temp
    return bubble(arr, index+1, lenght)

a=bubble(list2,0,len(list2))
print(a)

