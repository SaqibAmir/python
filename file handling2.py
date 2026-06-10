#Write a program to read the contents of a file and print them line by line.

with open ("Abc.txt","r") as f:
 for x in f:
    print(x)


#Create a file and write 5 names to it. Then read and display all the names.
with open ("bc.txt","w+") as n:
    n.write("saqib \n haseeb \n muneeb \n ameer\n shazia")

with open("bc.txt","r") as m:
    for g in m:
        print(g)

import os
if os.path.exists("bc.txt"):
    print("bc file exists")
else:
    print("bc file does not exist")

    
