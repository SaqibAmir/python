def bubble_sort(arr1):
    n=len(arr1)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr1[j] > arr1[j+1]:
                temp = arr1[j]
                arr1[j] = arr1[j+1]
                arr1[j+1] = temp
                swapped = True
        if not swapped:

            break
    print(f"Sorted array : {arr1}")
a=[1,3,55,7,5,4,3,23,33,43,0,3]


def bubble_sort2(arr1):
    top=len(arr1)-1
    print("before sorting")
    print(arr1)
    while top>0:
        for i in range(0,top):
            if arr1[i] > arr1[i+1]:
                temp = arr1[i]
                arr1[i] = arr1[i+1]
                arr1[i+1] = temp
        top=top-1
    print(f"after sorting {arr1}")
b=[1,3,55,7,5,4,3,23,33,43,0,3]

def bubble_sort3(arr1):
    swapped=True
    while swapped==True:
        swapped=False
        for i in range(0,len(arr1)-1):
            if arr1[i] > arr1[i+1]:
                temp = arr1[i]
                arr1[i] = arr1[i+1]
                arr1[i+1] = temp
                swapped = True
    print(f"Sorted array : {arr1}")
c=[1,3,55,7,5,4,3,23,33,43,0,3]

def bubble_sort4(arr1):
    swapped=True
    top =len(arr1)-1
    while top>0 and swapped ==True:
        for i in range(0,top):
            swapped=False
            if arr1[i] > arr1[i+1]:
                temp=arr1[i+1]
                arr1[i+1]=arr1[i]
                arr1[i]=temp
                swapped = True
            top=top-1
    print(f"Sorted array : {arr1}")
d=[1,3,55,7,5,4,3,23,33,43,0,3]

def bubble_sortay(d):
    swapped=True
    top=len(d)-1
    while top>0 and swapped==True:
        swapped=False
        for x in range (len(d)-1):
            if d[x]>d[x+1]:
                temp=d[x]
                d[x]=d[x+1]
                d[x+1]=temp
                swapped=True
        top=top-1
    print(d)
def bubblebubble(d):
    swapped=True
    top=len(d)-1
    while top>0 and swapped==True:
        swapped =False
        for x in range (0,len(d)-1):
            if d[x]>d[x+1]:
                temp=d[x]
                d[x]=d[x+1]
                d[x+1]=temp
                swapped=True
        top=top-1
    print(d)
bubblebubble(d)





