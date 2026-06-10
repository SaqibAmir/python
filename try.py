# print("start")
# a=10
# b=0
# try:
    
#     if b>5:
#       c=a/b
#     else:
#        c=a/b  
   
# except Exception as e:
#      print("error4",e)
# except NameError as e:
#      print("error3",e)
# except ValueError as e:
#    print("error2",e)
# except ZeroDivisionError as e:
#    print("error1",e)   
# finally:
#    print("execpt")            

#Write a program that asks the user for an integer and handles invalid input using try-except
# try:
#     n=int(input("Enter the integer : "))
#     if type(n)==int:
#       print("true")
#
# except Exception as e:
#     b=int(n)
#     print("true")
# Handle exceptions when converting a string to a float using float()
while True:
    try:
        n = float(input("input any thing: "))
        print("Float")
        break
    except Exception as e:
        print("please enter a float number")

    else:
        print("end")
m = ""
first_word = True

while True:
    if first_word:
        n = input("Enter the first word (must be a string): ")
        if n.isalpha():
            m += n
            first_word = False
            break
        else:
            print("First word must be alphabetic (string). Try again.")

