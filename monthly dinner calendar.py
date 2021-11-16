import random, datetime, calendar, keyboard

## Setting up date and time to the present
thePresent= datetime.datetime.now()

presentYear= thePresent.year

presentMonth= thePresent.month

theCalendar = calendar.Calendar()

monthDays2CalendarList=theCalendar.monthdays2calendar(presentYear, presentMonth)

#iterates the list of weeks in the month
for Week in monthDays2CalendarList:
    #iterates list of tuples of (date of month, day of the week)
    for days in Week:
        #if day of the week divided by 7 has a remainder of 0 == Monday and so on)
        #days[0]= day of the month (1-31)
        if days[1]%7==0:
            print(str(days[0])+" its Monday!")
        if days[1]%7==1:
            print(str(days[0])+" its Tuesday!")
        if days[1]%7==2:
            print(str(days[0])+" its Wednesday!")
        if days[1]%7==3:
            print(str(days[0])+" its Thursday!")
        if days[1]%7==4:
            print(str(days[0])+" its Friday!")
        if days[1]%7==5:
            print(str(days[0])+" its Saturday!")
        if days[1]%7==6:
            print(str(days[0])+" its Sunday!")


#dinner dictionary 1=mexican 2=grilled 3=italian 4=slow cooker 5=other
dinnerDict={0:"mexican", 1:"grill", 2:"baked", 3:"italian"}
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
bakedList=["fish","chicken"]
italianList=['Lasagna',
             'Raviolis and Zoodles',
             'Baked Mastaccoli',
             'Chicken parmesan',
             'Italian Sausage and pasta']



               
