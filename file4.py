#using end and format function
name="saqib"
lname="amir"
print(f"my name is :{name} {lname}",end="||")

try:

    a=int(input("please enter any number : "))
    if a>10:
         
       print(a+a)
except Exception as e:
    print(e)          
finally:
    print("finally")    