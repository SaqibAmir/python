#
# f=open("English.txt")
# c=open("Abc.txt","w")
# for x in range (1,25):
#   m=f.read()
#   c.write(m)
#   print(m)
#
# f.close
# c.close
# c=open("Abc.txt","r")
# print(c.read())
# c.close()
# #
# m=open("English.txt","a")
# m.write("""9) basically:
#         the use of besically can be used to describe in easiser words
#         -basically it will damage our envoirment- """)
from dataclasses import replace
#
# with open ("English.txt","r+") as f:
#     f.write("...")
#     for x in range (10):
#        f.write("helooo \n ")
# with open("English.txt","r") as f:
#
#     print(f.read())

# with open("practice.txt","w+") as f:
#     f.write("Hi everyone \n we are learning file I/O \n using Java \n I like programing Java")
#
# with open("practice.txt","r") as f:
#     data = f.read()
#     new_data=data.replace("Java","Python")
#     print(new_data)
#
#     if "learning" in new_data:
#         print("found")
#     else:
#         print("not found")
#
# def searching():
#
#         data=True
#         linenumber=1
#         with open("practice.txt","r") as f:
#             while data:
#                 data=f.read()
#                 if "learning" in data:
#                     print(linenumber)
#                     return
#             linenumber=linenumber+1
#         return -1
# searching()

# with open("numbers.txt","r+") as f:
#     data=f.read()
#     print(data)
#     num=""
#     for number in range(len(data)):
#         if data[number]==",":
#             print(int(num))
#             num=""
#         else:
#             num+=data[number]
#     nums=(data.split(","))
#
#     print(nums)
#     for m in (nums):
#         if int(m)%2==0:
#             print(int(m))
# f=open("bc.txt","r")
# c=open("English.txt","a")
# bb=f.read()
# c.write("ja ja tur jha")
#
# c.close()
# f.close()
# l=open("English.txt","r")
# print(l.read())
# l.close()
def searching():
    data = True
    line=0
    with open("English.txt", "r") as f:
        while data:

            data=f.read()
            if "saqib" in data:
                print(line)
                return
        line=line+1
    return -1
a=searching()
print(a)

# with open("practice.txt","r+") as f:
#      f.write("Hi everyone! \n we using java \n we are learning file handling \n i like programming in java ")
# with open ("practice.txt","r+") as f:
#     data=f.read()
#     new_data= data.replace("java","python")
#     print(new_data)
# with open("practice.txt","r") as f:
#     ner=f.read()
#     if "learning" in ner:
#         print("found")
#     else:
#         print ("not found")
#
# with open("practice.txt","r+") as f:
#     text = f.read()
#     text.replace("python","java")
#     print(text.count("java"))
#     text.title()
# with open("practice.txt","r") as u:
#     m=u.read()
#     print(m)
# with open("prctice.txt","x") as p:
#     p.write("Hello, world! \nWelcome to file handling in Python.")
# with open("prctice.txt","a") as i:
#     i.write("\n hello")
# def to_count():
#     try:
#         with open("practice.txt","r")as f:
#             text=f.read()
#             total=text.split()
#             lines=text.splitlines()
#             print("total words: ",len(total))
#             print("total lines: ",len(lines))
#     except FileNotFoundError:
#         print("File not found")
# #
# to_count()
# def ope1():
#      with open("practice.txt","r") as f , open ("english.txt","w") as g:
#          text=f.read()
#          for line in text:
#              if line.strip():
#                  g.write(line)
#      with open("english.txt","w") as u:
#          u.write(text)
# ope1()
