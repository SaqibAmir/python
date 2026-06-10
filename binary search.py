Array = [11,12,13,15,14,18,16,999,17,19,20,21]
def insertion():
    global Array
    n=len(Array)
    for x in range(1,n):
        key=Array[x]
        j=x-1
        while j>=0 and Array[j]>key:
            Array[j+1]=Array[j]
            j=j-1
        Array[j+1]=key

def BinarySearch(tar):
    global Array
    low=0
    high=len(Array)
    found=False
    while high>=low and found==False:
        mid=int((low+high)/2)
        if Array[mid] == tar:
           print("Found at : ",mid)
           found=True
        elif Array[mid]>tar:
            high=mid-1
        else:
            low=mid+1

def recursiveBinary(tar,low,high):
    global Array
    if high>=low:
        mid=int((low+high)/2)
        if Array[mid]==tar:
            return "found"
        elif Array[mid]>tar:
            return recursiveBinary( tar, low, mid-1)
        else:
            return recursiveBinary( tar, mid+1, high)
    else:
        return "Not found"

def linearSearch(tar):
    global Array
    for x in range(len(Array)):
        if Array[x]==tar:
            print("Found")

def BubbleSort():
    global Array
    boundary=len(Array)-1
    found=False
    while found ==False and boundary>0:
        found=True
        for x in range(boundary):
            if Array[x]<Array[x+1]:
                Array[x],Array[x+1]=Array[x+1],Array[x]
            found=False
        boundary=boundary-1
insertion()
print(Array)
BubbleSort()
print(Array)