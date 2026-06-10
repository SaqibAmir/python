stack=[]
def Enqueue():
    global stack
    n=input("Enter anything you want to add in stack : ")
    stack.append(n)
def Dequeue():
    global stack
    stack.pop()
def Display():
    global stack
    print(f"Your stack is {stack}")
while True:
    print("1.Enqeue\n2.Dequeue\n3.Display\n4.Exit")
    m=int(input("What do you want : "))
    if m==1:
        Enqueue()
    elif m==2:
        Dequeue()
    elif m==3:
        Display()
    elif m==4:
        break
    else:
        break
#Question
global stackData
global stackpointer
stackData=[0]*10
stackpointer=0

def output():
    global stackData
    global stackpointer
    for x in stackData:
        print(x)
    print(stackpointer)

def push(value):
    global stackpointer
    global stackData
    if stackpointer>9:
        return False
    else:
        stackData[stackpointer]=value
        stackpointer=stackpointer+1
        return True
for x in range(11):
    value=input("Enter : ")
    temp=push(value)
    if temp==True:
        print(f"The value {value} is added to stack")
    else:
        print("the value is not added")

def pop():
    global stackData
    global stackpointer
    if stackpointer==0:
        return -1
    else:
        stackpointer=stackpointer-1
        return stackData[stackpointer]