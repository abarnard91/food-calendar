import datetime
import calendar

loop=False
innerLoop=False
thePresent= datetime.datetime.now()

presentYear= thePresent.year
#presentYear= 2022

presentMonth= thePresent.month
#presentMonth= 2
##pretty straight forward
print( "The month is " + str(presentMonth) + " and the year is " + str(presentYear))

##prints the calendar of the current month and current year
print( calendar.month(presentYear, presentMonth))

##iteration of days in the current month (lists 0 for days not in month through end of month (ie 28,30 or 31))

obj = calendar.Calendar()

#for day in obj.itermonthdays(presentYear, presentMonth):
    #print(day)


##monthdayclaendar makes a list of the weeks and those weeks are a list of the dates
monthDayCalendarList=obj.monthdayscalendar(presentYear, presentMonth)
#print(monthDayCalendarList[0][0])


##monthDays2Calender makes a list of weeks and in those weeks are lists of days like above but instead are made of tuples of date and day of the week (0=mon 6=sun)

monthDays2CalendarList=obj.monthdays2calendar(presentYear, presentMonth)


#print (monthDays2CalendarList[0])
#mondayDays2Calendar[0]=week11 list, [2}=3rd day in the of the in the week (as a tuple of date and day of the week) [1]=2nd number in the tuple (the day of the week)
#print (monthDays2CalendarList[0][2][1])

## Big loop that if you want to retry picking dinners for the month 
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
                    
