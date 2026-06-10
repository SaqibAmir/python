from PIL import Image
def viewer(n):
    if n=="yes" or n=="Yes":

      image=Image.open("C:\\Users\\Saqib PC\\Pictures\\Camera Roll\\IMG20221207130259.jpg")
      image.show()

    else:
       print("Nothing") 
n=str(input("Do you want to see image : "))       
viewer(n)