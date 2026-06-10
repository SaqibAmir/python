# chapter 1 linear search
# question no.1
# part 1
TheData=[20,3,4,8,12,99,4,26,4]
# part 2
def search(TheData):
    whole_number=int(input("Enter the whole number: "))
    for x in TheData:
        if x==whole_number:
            print("Found")
            return True
    print("Not Found")
    return False
search(TheData)
## question 2
## part 1
arraydata=[10,5,6,7,1,12,13,15,21,8]
# part 2
def linearSearch(num):
    for x in range(len(arraydata)):
        if arraydata[x]==num:
            return True
    return False
## part 3
arraydata=[10,5,6,7,1,12,13,15,21,8]
n=int(input("Enter the number"))
a=linearSearch(n)
if a==True:
    print("Found")
elif a==False:
     print("Not Found")

#question 3
# part 1

