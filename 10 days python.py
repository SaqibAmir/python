# #Session 1
# #(a)(i)
# class vehicle:
#     def __init__(self,ID,MaxSpeed,IncraseAmount):
#         #Private ID : STRING
#         #PRIVATE MAXSPEED : INTEGER
#         #PRIVATE CURRENTSPEED : INTEGER
#         #PRIVATE INCREASEAMOUNT : INTEGER
#         #PRIVATE HORIZONTALPosition : INTEGER
#
#         self.__id=ID
#         self.__maxspeed=MaxSpeed
#         self.__IncreaseAmount=IncraseAmount
#         self.__CurrentSpeed=0
#         self.__HorizontalPosition=0
#
# #(a)(ii)
#     def GetCurrentSpeed(self):
#         return self.__CurrentSpeed
#     def GetIncreaseAmount(self):
#         return self.__IncreaseAmount
#     def GetMaxSpeed(self):
#         return self.__maxspeed
#     def GetHorizontalPosition(self):
#         return self.__HorizontalPosition
# #(a)(iii)
#     def SetCurrentSpeed(self,NewSetCurrentSpeed):
#         self.__CurrentSpeed=NewSetCurrentSpeed
#     def SetHorizontalPosition(self,NewSetHorizontalPosition):
#         self.__HorizontalPosition=NewSetHorizontalPosition
# #(iv)
#     def IncreaseSpeed(self):
#         self.__CurrentSpeed=self.__CurrentSpeed+self.__IncreaseAmount
#         if self.__CurrentSpeed>self.__maxspeed:
#             self.__CurrentSpeed=self.__maxspeed
#         self.__HorizontalPosition=self.__HorizontalPosition+self.__CurrentSpeed
#     def Display(self):
#         print("The Horizontal Position is : ",self.__HorizontalPosition)
#         print("The Current Speed : ",self.__CurrentSpeed)
# #(b)(i)
# class Helicopter(vehicle):
#     def __init__(self,ID,MaxSpeed,IncraseAmount,VerticalChange,MaxHeight):
#         super().__init__(ID,MaxSpeed,IncraseAmount)
#         self.__VerticalPosition=0
#         self.__VerticalChange=VerticalChange
#         self.__MaxHeight=MaxHeight
# #(b)(ii)
#     def IncreaseSpeed(self):
#         super().IncreaseSpeed()
#         self.__VerticalPosition=self.__VerticalPosition+self.__VerticalChange
#         if self.__VerticalChange> self.__MaxHeight:
#             self.__VerticalChange=self.__MaxHeight
# #(c)
#     def Display(self):
#         super().Display()
#         print("The Vertical Position Is : ",self.__VerticalPosition)
#
# # car=vehicle("Tiger",100,20)
# # helicop=Helicopter("Lion",350,40,3,100)
# # car.IncreaseSpeed()
# # car.IncreaseSpeed()
# # car.Display()
# # helicop.IncreaseSpeed()
# # helicop.IncreaseSpeed()
# # helicop.Display()
#
#
# #Session 2
# #(a)(i)
# class Card:
#     def __init__(self,Number,Colour):
#         #Number:INTEGER
#         #Colour : STRING
#         self.__number=Number
#         self.__colour=Colour
# #(b)(ii)
#     def GetNum(self):
#         return self.__number
#     def GetColour(self):
#         return self.__colour
# #(b)(iii)
# onered=Card(1,"red")
# twored=Card(2,"red")
# threered=Card(3,"red")
# fourthred=Card(4,"red")
# fivered=Card(5,"red")
# oneblue=Card(1,"blue")
# twoblue=Card(2,"blue")
# threeblue=Card(3,"blue")
# fourblue=Card(4,"blue")
# fiveblue=Card(5,"Blue")
# oneyellow=Card(1,"yellow")
# twoyellow=Card(2,"yellow")
# threeyellow=Card(3,"yellow")
# fouryellow=Card(4,"yellow")
# fiveyellow=Card(5,"yellow")
# #(b)(i)
# class Hand:
#
#     def __init__(self,card1,card2,card3,card4,card5):
#         self.__array=[]
#         self.__array.append(card1)
#         self.__array.append(card2)
#         self.__array.append(card3)
#         self.__array.append(card4)
#         self.__array.append(card5)
#         self.__FirstCard=0
#         self.__NumberCard=5
# #(b)(ii)
#     def GetCard(self,index):
#         return self.__array[index]
#
# #(b)(iii)
# player1=Hand(onered,twored,threered,fourthred,oneyellow)
# player2=Hand(twoyellow,threeyellow,fouryellow,fiveyellow,oneblue)
#
# #(c)(i)
# def CalculateValue(handobject):
#     player_score=0
#     for x in range(5):
#         playercard=handobject.GetCard(x)
#         colour=playercard.GetColour()
#         numbers=playercard.GetNum()
#         if colour=="red":
#             player_score=player_score+5
#         elif colour=="blue":
#             player_score=player_score+10
#         elif colour=="yellow":
#             player_score=player_score+15
#
#         player_score=player_score+numbers
#     return player_score
# a=CalculateValue(player1)
# b=CalculateValue(player2)
# if a>b:
#     print("player one wins")
# else :
#     print("player two wins")
#
# #Session 3
# #(a)
# class Character:
#     def __init__(self,name,x,y):
#         #Private Name : STRING
#         #Private XCoordinate : INTEGER
#         #Private YCoordinate : INTEGER
#         self.__Name=name
#         self.__XCoordinate=x
#         self.__YCoordinate=y
#
# #(b)
#     def GetName(self):
#         return self.__Name
#     def GetX(self):
#         return self.__XCoordinate
#     def GetY(self):
#         return self.__YCoordinate
# #(c)
#     def ChangePosition(self,XChange,YChange):
#         self.__XChange=XChange
#         self.__YChange=YChange
#
#         self.__XCoordinate=self.__XCoordinate+self.__XChange
#         self.__YCoordinate=self.__YCoordinate+self.__YChange
# #(d)
# character=[]
# try:
#     file=open("Character.txt","r")
#     for x in range(10):
#         name=file.readline().strip()
#         xcoor=int(file.readline().strip())
#         ycoor=int(file.readline().strip())
#         Character_object=Character(name,xcoor,ycoor)
#         character.append(Character_object)
# except:
#     print("File doesnot exist")
# print(character)
#
# #(e)
# flag=False
# while flag==False:
#     user=input("Enter your name : ")
#     for x in range(10):
#         name=character[x].GetName()
#         if name.lower()==user.lower():
#             position=x
#             flag=True
#
# print(position)
#
# flag = False
# while flag == False:
#     move = input("INPUT THE MOVE A , W , S , D : ")
#
#     if move.upper() == "A":
#         character[position].ChangePosition(-1,0)
#         flag=True
#     elif move.upper() == "W":
#         character[position].ChangePosition(0,1)
#         flag=True
#     if move.upper() == "S":
#         character[position].ChangePosition(0,-1)
#         flag=True
#     elif move.upper() == "D":
#         character[position].ChangePosition(1,0)
#         flag=True
#
# print(character[position].GetName(),"has changed coordnates to x = ",character[position].GetX(),"and y = ",character[position].GetY())
#
# #Session 6
# #(a)(i)
#
#
# import datetime
#
#
# class Character():
#     # PRIVATE CharacterName : STRING
#     # PRIVATE DateOfBirth : DATE
#     # PRIVATE Intelligence : REAL
#     # PRIVATE Speed : INTEGER
#
#     def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP):
#         self.__CharacterName = CharacterNameP
#         self.__DateOfBirth = DateOfBirthP  # DATE
#         self.__Intelligence = IntelligenceP
#         self.__Speed = SpeedP
#
#     def GetIntelligence(self):
#         return self.__Intelligence
#
#     def GetName(self):
#         return self.__CharacterName
#
#     def SetIntelligence(self, newintelligence):
#         self.__Intelligence = newintelligence
#
#     def Learn(self):
#         increasedvalue = self.__Intelligence * 0.1
#         self.__Intelligence = self.__Intelligence + increasedvalue
#
#     def ReturnAge(self):
#         Age = 2023 - self.__DateOfBirth.year
#         return Age
#
#
# class MagicCharacter(Character):
#     # PRIVATE Element : STRING
#
#     def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP, ElementP):
#         super().__init__(CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP)
#         self.__Element = ElementP
#
#     def Learn(self):
#         if self.__Element == "fire" or self.__Element == "water":
#             increasedvalue = super().GetIntelligence() * 0.2
#             newintelligence = super().GetIntelligence() + increasedvalue
#
#         elif self.__Element == "earth":
#             increasedvalue = super().GetIntelligence() * 0.3
#             newintelligence = super().GetIntelligence() + increasedvalue
#         else:
#             increasedvalue = super().GetIntelligence() * 0.1
#             newintelligence = super().GetIntelligence() + increasedvalue
#
#         super().SetIntelligence(newintelligence)
# #(b)(i)
#
# FirstCharacter=Character("Royal",datetime.datetime(2019,1,1),70,30)
# FirstCharacter.Learn()
# character1=FirstCharacter.GetName()
# age=FirstCharacter.ReturnAge()
# int=FirstCharacter.GetIntelligence()
# print("The",character1,"is",age,"Years old and its intelligence is ",int)
#
# FirstMagic=MagicCharacter("Light",datetime.datetime(2018,3,3),75,22,"fire")
# FirstCharacter.Learn()
# character2=FirstMagic.GetName()
# age2=FirstMagic.ReturnAge()
# int2=FirstMagic.GetIntelligence()
# print("The",character2,"is",age2,"Years old and its intelligence is ",int2)

#Session 4
#(1)(a)
global Animals
Animals=[""]*10
#(1)(b)
Animals[0] = "horse"
Animals[1] = "lion"
Animals[2] = "rabbit"
Animals[3] = "mouse"
Animals[4] = "bird"
Animals[5] = "deer"
Animals[6] = "whale"
Animals[7] = "elephant"
Animals[8] = "kangaroo"
Animals[9] = "tiger"


#(1)(c)
def SortDecending():
    global Animals
    Arraylenght=len(Animals)
    for x in range(0,Arraylenght):
        for y in range(0,Arraylenght-x-1):
            if Animals[y][0]<Animals[y+1][0]:
                temp=Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1]=temp

SortDecending()

for x in range(len(Animals)):
    print(Animals[x])

#Second Question
#(1)(a)(i)
#Declaration of Array
DataArray=[]
#(1)(a)(ii)(iii)
try:
    file=open("QueueData.txt", "r")
    for x in range(25):
        line=int(file.readline().strip())
        DataArray.append(line)
    file.close()
except IOError:
    print("File doesnot Exist")

def PrintArray(integer):
    finalstring=""
    for x in range(25):
        finalstring=finalstring+str(integer[x])+" "
    print(finalstring)

PrintArray(DataArray)

#(1)(c)
def LinearSearch(arr, integer):
    count=0
    for x in range (25):
        if DataArray[x]==integer:
            count=count+1
    return count

input1=False
while input1==False:
    target=int(input("Enter number between 0 and 100 inclusve : "))
    if target>=0 and target<=100:
        input1=True
times=LinearSearch(DataArray,target)

print("the number ",target," is found ",times," times")

#To allow sometthing Different


