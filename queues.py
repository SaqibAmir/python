global startpointer
global endpointer
global numberofitems
global array

startpointer=0
endpointer=0
numberofitems=0
array=[""]*10

def enqueue(value):
    global numberofitems
    global endpointer
    global startpointer
    global array

    if numberofitems > 10:
        print("array is full")
    else:
        array[endpointer] = value
        endpointer = endpointer + 1
        if endpointer > 9:
            endpointer = 0
    numberofitems = numberofitems + 1
    print(array)

def dequeue():
    global numberofitems
    global endpointer
    global startpointer
    global array

    if numberofitems == 0:
        print("array is empty")
    else:
        value = array[startpointer]
        startpointer = startpointer + 1
        print(value)
        if startpointer > 9:
            startpointer = 0
    numberofitems = numberofitems - 1
    print(array)
def display():
    global numberofitems
    global endpointer
    global startpointer
    global array
    print(
        f"the startpointer is at {startpointer}, the enpointer is at {endpointer} and there are {numberofitems} number of items")

