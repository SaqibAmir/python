def prime(n):
    found=False
    try:       
       if n%2==0:
           found=True 
           return found
       else:
           found=False
           return found
    except Exception as e:
        print(e)   
n=int(input("enter any number"))
if prime(n)==False:
    print("not a prime num")
else:
    print("prime num")    


