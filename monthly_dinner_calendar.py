import random
import datetime
import calendar
from tkinter import *
from PIL import ImageTk, Image
#from GUI_practice import *

#keyboard
loop=False
innerLoop=False
## Setting up date and time to the present
thePresent= datetime.datetime.now()

presentYear= thePresent.year

presentMonth= thePresent.month
#presentMonth=7

theCalendar = calendar.Calendar()

monthDays2CalendarList=theCalendar.monthdays2calendar(presentYear, presentMonth)


if presentMonth==1:
    presentMonth="January"
if presentMonth==2:
    presentMonth="February"
if presentMonth==3:
    presentMonth="March"
if presentMonth==4:
    presentMonth="April"
if presentMonth==5:
    presentMonth="May"
if presentMonth==6:
    presentMonth="June"
if presentMonth==7:
    presentMonth="July"
if presentMonth==8:
    presentMonth="August"
if presentMonth==9:
    presentMonth="September"
if presentMonth==10:
    presentMonth="October"
if presentMonth==11:
    presentMonth="November"
if presentMonth==12:
    presentMonth="December"




window=Tk()
window.title("hello world")
#Size of the full window
window.geometry("1200x800")
window.configure(background="grey")

##Resize a JPEG image

canvas=Canvas(window, width=1000, height= 800)
canvas.pack()

##Image file
path= "blank calendar.jpg"
#open image file as variable img
img=(Image.open(path))

#actual resizing 
resizedImage= img.resize((1000,800), Image.ANTIALIAS)
newImage=ImageTk.PhotoImage(resizedImage)


canvas.create_image(10,10, anchor=NW, image=newImage)

monthImage=Label(window, text=((presentMonth +" "+ str(presentYear))), font=("Arial", 40), anchor=CENTER, background="white")

monthImage.pack()

canvas.create_window(512,93, window=monthImage)



x=170
y=166
calendarCounter=0



def calendarDateNumber(date, x, y):
     
    date=Label(window, text=(str(date)), font=("Arial",14), anchor=CENTER, background="white")
    date.pack()
    canvas.create_window(x, y, window=date)










#dinner dictionary 0=mexican 1=grilled 2=baked dinners 3=italian 4=breakfast 5=slow cooker 6= pizza 7= asian
dinnerDict={0:"mexican", 1:"grill", 2:"baked", 3:"italian", 4:"breakfast",5:"crockpot", 6:"pizza", 7:"asian"}
mexicanList=['Chicken Tacos',
             'Beef Tacos',
             'Ground Turkey Tacos',
             'Enchiladas',
             'Mexican Stuffed Peppers',
             'Salsa Chicken',
             'Chicken Quesadillas',
             'Loaded Nachos']

backUpMexicanList=[]

grillList=['Cheeseburgers',
           'Impossible Burgers',
           'Black Bean Burgers',
           'Grilled Chicken Patties',
           'Chicken Wings', 
           'Chicken Thighs',
           'Chicken Breasts',
           'Chicken DrumSticks',
           'PorkChops',
           'Steaks',
           'Bratwursts',
           'Chicken Sausages']

backUpGrillList=[]

bakedList=["fish",
           "chicken",
           "shepherds pie",
           "casserole"]
           
backUpBakedList=[]

italianList=['Lasagna',
             'Raviolis and Zoodles',
             'Baked Mastaccoli',
             'Chicken parmesan',
             'Italian Sausage and pasta',
             'Stuffed shells',
             'Italian stuffed Peppers']
             
backUpItalianList=[]
             
breakfastList=[ "quiche loreine",
                "breakfast casserole",
                "french toast",
                "Eggs and pancakes",
                "Belgum Waffles"]
                
backUpBreakfastList=[]
                
crockpotList=[  "Crockpot chili",
                "Ribs",
                "Chicken Tortilla Soup",
                "Tortellini soup",
                "Chicken, Carrots and potatos",
                "Beef roast",
                "Pork Roast"]
                
backUpCrockpotList=[]
                
pizzaList= ["thin crust", 
            "Giordanos deep dish", 
            "Lou malnatis deep dish", 
            "cauliflower crust pizza",
            "BBQ chicken Pizza"] 
            
backUpPizzaList=[]


asianList=["orange chicken and cauliflower fried rice",
           "Chicken stirfry",
           "Dumplings and fried rice",
           "potstickers and japanese fried rice"]

backUpAsianList=[]

           

#empty list that has random dinners from randomDinner function appended to it to store
#the randomized dinners as an individual variable as the dinner variable is recycled each iteration
#for some reason this needs to be declared as a global variable outside the function to work, but counter needs to be declared global inside the function
#global randomDinnersList
randomDinnersList=[]
#simple counter that increases by 1 every iteration of the for loop (coinsides with the date of the month)
counter=0
def randomDinner(meal,backup):
    global counter
    #global mexicanList, grillList, bakedList, italianList, breakfastList, crockpotList, pizzaList, asianList
    #global backUpMexicanList, backUpGrillList, backUpBakedList, backUpItalianList, backUpBreakfastList, backUpCrockpotList, backUpPizzaList, backUpAsianList
    
    if len(meal) !=0:
        dinner=random.choice(meal)
        meal.remove(dinner)
        backup.append(dinner)
        randomDinnersList.append(dinner)
        print(dinner)
        #print(randomDinnersList[counter])
        #print(randomDinnersList)
        #return randomDinnersList
        counter+=1
        
    else:
        print("list reboot")
        meal.extend(backup)
        backup.clear()
        dinner=random.choice(meal)
        meal.remove(dinner)
        backup.append(dinner)
        randomDinnersList.append(dinner)
        print(dinner)
        #print (randomDinnersList[counter])
        #print(randomDinnersList)
        counter+=1
            
            
def dinnerPicker():

    dinnerDictList=[]
    for k in dinnerDict.keys():
        dinnerDictList.append(k)
    dinnerTypePicker=random.randint(0,7)
    #dinnerTypePicker=7
    if dinnerTypePicker == dinnerDictList[0]:
        print("we're having mexican")
        randomDinner(mexicanList,backUpMexicanList)
    
    if dinnerTypePicker == dinnerDictList[1]:
        print("we're having grilled food")
        randomDinner(grillList,backUpGrillList)
        
    if dinnerTypePicker == dinnerDictList[2]:
        print("we're having baked food")
        randomDinner(bakedList,backUpBakedList)
        
    if dinnerTypePicker == dinnerDictList[3]:
        print("we're having italian food")
        randomDinner(italianList,backUpItalianList)
        
    if dinnerTypePicker == dinnerDictList[4]:
        print("we're having Breakfast food")
        randomDinner(breakfastList,backUpBreakfastList)

    if dinnerTypePicker == dinnerDictList[5]:
        print("we're having slow cooker food")
        randomDinner(crockpotList,backUpCrockpotList)
        
    if dinnerTypePicker == dinnerDictList[6]:
        print("we're having pizza!!!")
        randomDinner(pizzaList,backUpPizzaList)

    if dinnerTypePicker == dinnerDictList[7]:
        print("We're having asian!")
        randomDinner(asianList, backUpAsianList)

while loop==False:


    #monthImage=Label(window, text=((presentMonth +" "+ str(presentYear))), font=("Arial", 40), anchor=CENTER, background="white")
    ##iterates the list of weeks in the month
    for Week in monthDays2CalendarList:
        ##iterates list of tuples of (date of month, day of the week)
        #print(Week)
##        print(Week[6][1])
##        calendarDateNumber(Week[6][1],x,y)
##        x+=130
##        calendarCounter+=1
##        if counter>6:
##            y+=121
##            x=170
##            calendarCounter=0
##            calendarCounter+=1
##        
        
        
        if innerLoop==False:
            
            ##inner loop to allow week to be redone if you don't like dinner choices
            for days in Week:
                ##if day of the week divided by 7 has a remainder of 0 == Monday and so on)
                ##days[0]= day of the month (1-31)
        
                if days[1]%7==0:
                    print(str(days[0])+" its Monday!")
                    x=300
                    
                    calendarDateNumber(days[0],x,y)
                    
                    calendarCounter+=1
                    if calendarCounter>7:
                        y+=121
                        #x=170
                        calendarCounter=0
                        calendarCounter+=1
                    dinnerPicker()
                    
                if days[1]%7==1:
                    print(str(days[0])+" its Tuesday!")
                    x=430
                    calendarDateNumber(days[0],x,y)
                    
                    calendarCounter+=1
                    if calendarCounter>7:
                        y+=121
                        #x=170
                        calendarCounter=0
                        calendarCounter+=1
                    dinnerPicker()
                    
                if days[1]%7==2:
                    print(str(days[0])+" its Wednesday!")
                    x=560
                    calendarDateNumber(days[0],x,y)
                    
                    calendarCounter+=1
                    if calendarCounter>7:
                        y+=121
                       # x=170
                        calendarCounter=0
                        calendarCounter+=1
                    dinnerPicker()
                    
                if days[1]%7==3:
                    print(str(days[0])+" its Thursday!")
                    x=690
                    
                    calendarDateNumber(days[0],x,y)
                    
                    calendarCounter+=1
                    if calendarCounter>7:
                        y+=121
                       # x=170
                        calendarCounter=0
                        calendarCounter+=1
                    dinnerPicker()
                    
                if days[1]%7==4:
                    print(str(days[0])+" its Friday!")
                    x=820
                    
                    calendarDateNumber(days[0],x,y)
                    
                    calendarCounter+=1
                    if calendarCounter>7:
                        y+=121
                       # x=170
                        calendarCounter=0
                        calendarCounter+=1
                    dinnerPicker()
                    
                if days[1]%7==5:
                    print(str(days[0])+" its Saturday!")
                    x=950
                    
                    calendarDateNumber(days[0],x,y)
                    
                    calendarCounter+=1
                    if calendarCounter>7:
                        y+=121
                        #x=170
                        calendarCounter=0
                        calendarCounter+=1
                    dinnerPicker()
                    
                if days[1]%7==6:
                    print(str(days[0])+" its Sunday!")
                    x=170
                    #this makes sure the calendar sets the date numbers in the right boxes at the 1st full week.
                    if days[0] <8 and days[0]>1:
                        y=287
                        calendarCounter=1
                       


                    
                    calendarDateNumber(days[0],x,y)
                    #x+=130
                    calendarCounter+=1
                    if calendarCounter>7:
                        y+=121
                        #x=170
                        calendarCounter=0
                        calendarCounter+=1
                    dinnerPicker()
            

        ## This pauses the for loop at the week level to check if you like the dinner choices    
    
            if Week[6][1]==6:
                userChoice=str(input("do you want to continue?"))
                if userChoice=="yes":
                    print("Okie Dokie")
                    continue
                    innerLoop==True
                else:
                    retry=str(input("do you want to retry?"))
                    if retry=="yes":
                        print("Back to the top")
                        break
                    else:
                        print("bye")
                        window.mainloop()
                        loop=True
                        innerLoop=True
                        break

#window.mainloop()
                    
