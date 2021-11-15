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
theDinnerDict={"Chicken Tacos": 1,
               "Beef Tacos": 1,
               "Ground Turkey Tacos": 1,
               "Enchiladas": 1,
               "Mexican Stuffed Peppers":1,
               "Salsa Chicken":1,
               "Chicken Quesadillas":1,
               "Loaded Nachos":1,

               "Cheeseburgers":2,
               "Impossible Burgers":2,
               "Black Bean Burgers":2,
               "Grilled Chicken Patties":2,
               "Chicken Wings":2,
               "Chicken Thighs":2,
               "Chicken Breasts":2,
               "Chicken DrumSticks":2,
               "PorkChops":2,
               "Steaks":2,
               "Bratwursts":2,
               "Chicken Sausages":2,

               "Lazagna":3,
               "Raviolis and Zoodles":3,
               "Baked Mastaccoli":3,
               "Chicken parmesan":3,
               "Italian Sausage and pasta":3


               }
               



               
