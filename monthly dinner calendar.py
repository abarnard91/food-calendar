import random
import datetime
import calendar

#keyboard
loop=False
innerLoop=False
## Setting up date and time to the present
thePresent= datetime.datetime.now()

presentYear= thePresent.year

presentMonth= thePresent.month

theCalendar = calendar.Calendar()

monthDays2CalendarList=theCalendar.monthdays2calendar(presentYear, presentMonth)




#dinner dictionary 0=mexican 1=grilled 2=baked dinners 3=italian 4=breakfast 5=slow cooker
dinnerDict={0:"mexican", 1:"grill", 2:"baked", 3:"italian", 4:"breakfast",5:"crockpot", 6:"pizza"}
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

#empty list that has random dinners from randomDinner function appended to it to store
#the randomized dinners as an individual variable as the dinner variable is recycled each iteration
#for some reason this needs to be declared as a global variable outside the function to work, but counter needs to be declared global inside the function
global randomDinnersList
randomDinnersList=[]
#simple counter that increases by 1 every iteration of the for loop (coinsides with the date of the month)
counter=0
def randomDinner(meal,backup):
    global counter
    if len(meal) !=0:
        dinner=random.choice(meal)
        meal.remove(dinner)
        backup.append(dinner)
        randomDinnersList.append(dinner)
        print(dinner) 
        print(randomDinnersList[counter])
        #print(randomDinnersList)
        return randomDinnersList
        counter+=1
        
    else:
        print("list reboot")
        meal=backup
        dinner=random.choice(meal)
        meal.remove(dinner)
        backup.append(dinner)
        randomDinnersList.append(dinner)
        print(dinner)
        print (randomDinnersList[counter])
        #print(randomDinnersList)
        return randomDinnersList
        counter+=1
            
            
def dinnerPicker():

    dinnerDictList=[]
    for k in dinnerDict.keys():
        dinnerDictList.append(k)
    dinnerTypePicker=random.randint(0,6)
    #dinnerTypePicker=0
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

while loop==False:
    
    ##iterates the list of weeks in the month
    for Week in monthDays2CalendarList:
        ##iterates list of tuples of (date of month, day of the week)
        #print(Week)
        #print(Week[6][1])
        
        

        if innerLoop==False:
            ##inner loop to allow week to be redone if you don't like dinner choices
            for days in Week:
                ##if day of the week divided by 7 has a remainder of 0 == Monday and so on)
                ##days[0]= day of the month (1-31)
        
                if days[1]%7==0:
                    print(str(days[0])+" its Monday!")
                    dinnerPicker()
                    
                if days[1]%7==1:
                    print(str(days[0])+" its Tuesday!")
                    dinnerPicker()
                    
                if days[1]%7==2:
                    print(str(days[0])+" its Wednesday!")
                    dinnerPicker()
                if days[1]%7==3:
                    print(str(days[0])+" its Thursday!")
                    dinnerPicker()
                if days[1]%7==4:
                    print(str(days[0])+" its Friday!")
                    dinnerPicker()
                if days[1]%7==5:
                    print(str(days[0])+" its Saturday!")
                    dinnerPicker()
                if days[1]%7==6:
                    print(str(days[0])+" its Sunday!")
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
                        loop=True
                        innerLoop=True
                        break
                    
