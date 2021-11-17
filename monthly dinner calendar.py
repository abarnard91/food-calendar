import random
import datetime
import calendar
#keyboard

## Setting up date and time to the present
thePresent= datetime.datetime.now()

presentYear= thePresent.year

presentMonth= thePresent.month

theCalendar = calendar.Calendar()

monthDays2CalendarList=theCalendar.monthdays2calendar(presentYear, presentMonth)




#dinner dictionary 0=mexican 1=grilled 2=baked dinners 3=italian 4=breakfast 5=slow cooker
dinnerDict={0:"mexican", 1:"grill", 2:"baked", 3:"italian", 4:"breakfast",5:"crockpot"}
mexicanList=['Chicken Tacos',
             'Beef Tacos',
             'Ground Turkey Tacos',
             'Enchiladas',
             'Mexican Stuffed Peppers',
             'Salsa Chicken',
             'Chicken Quesadillas',
             'Loaded Nachos']
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
bakedList=["fish",
           "chicken"]
italianList=['Lasagna',
             'Raviolis and Zoodles',
             'Baked Mastaccoli',
             'Chicken parmesan',
             'Italian Sausage and pasta',
             'Stuffed shells',
             'Italian stuffed Peppers']
breakfastList=[ "quiche loreine",
                "breakfast casserole",
                "french toast",
                "Eggs and pancakes",
                "Belgum Waffles"]
crockpotList=[  "Crockpot chili",
                "Ribs",
                "Chicken Tortilla Soup",
                "Tortellini soup",
                "Chicken, Carrots and potatos",
                "Beef roast",
                "Pork Roast"]
def dinnerPicker():
    global dinnerDict
    global mexicanList
    global grillList
    global bakedList
    global italianList
    global breakfastList
    global crockpotList
    dinnerDictList=[]
    for k in dinnerDict.keys():
        dinnerDictList.append(k)
    dinnerTypePicker=random.randint(0,5)
    if dinnerTypePicker == dinnerDict[0]:
        print("we're having mexican")
        dinner=random.choice(mexicanList)
        print(dinner)
    if dinnerTypePicker == dinnerDict[1]:
        print("we're having grilled food")
        dinner=random.choice(grillList)
        print(dinner)
    if dinnerTypePicker == dinnerDict[2]:
        print("we're having baked food")
        dinner=random.choice(bakedList)
        print(dinner)
    if dinnerTypePicker == dinnerDict[3]:
        print("we're having italian food")
        dinner=random.choice(italianList)
        print(dinner)
    if dinnerTypePicker == dinnerDict[4]:
        print("we're having Breakfast food")
        dinner=random.choice(breakfastList)
        print(dinner)
    if dinnerTypePicker == dinnerDict[5]:
        print("we're having slow cooker food")
        dinner=random.choice(crockpotList)
        print(dinner)

#iterates the list of weeks in the month
for Week in monthDays2CalendarList:
    #iterates list of tuples of (date of month, day of the week)
    for days in Week:
        #if day of the week divided by 7 has a remainder of 0 == Monday and so on)
        #days[0]= day of the month (1-31)
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
