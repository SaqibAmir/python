# #linear search
# TheData=[20,3,4,8,12,99,4,26,4]
# def search ():
#     n=int(input("Input the number : "))
#     for number in range(0,len(TheData)):
#         if TheData[number]==n :
#             print("found")
#             return True
#     print("Not found")
#     return False
# b=search()
# arraydata=[10,5,6,7,1,12,13,15,21,8]
# def linearSearch(num):
#     for x in range(0,len(arraydata)):
#         if arraydata[x]==num:
#             return True
#     return False
#
# num1=int(input("Input the number you want to search : "))
# a=linearSearch(num1)
# if a = True:
#     print("founded")
# else:
#     print("Not Founded")
global DataArray
DataArray=[0]*100
def  FindValues():
  global DataArray
  try:
    f=open("IntegerData.txt" ,"r")
    for x in range(0,100):
       DataArray[x]=f.readline()
       DataArray[x].rstrip('\n')
       DataArray[x]=int(DataArray[x])
    f.close()
  except IOError:
    print("file not found")
FindValues()
print(DataArray)

