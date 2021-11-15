import datetime
import calendar

thePresent= datetime.datetime.now()

presentYear= thePresent.year

#presentMonth= thePresent.month
presentMonth= 2
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
print(monthDayCalendarList[0][0])


##monthDays2Calender makes a list of weeks and in those weeks are lists of days like above but instead are made of tuples of date and day of the week (0=mon 6=sun)

monthDays2CalendarList=obj.monthdays2calendar(presentYear, presentMonth)


print (monthDays2CalendarList[0])
#mondayDays2Calendar[0]=week11 list, [2}=3rd day in the of the in the week (as a tuple of date and day of the week) [1]=2nd number in the tuple (the day of the week)
print (monthDays2CalendarList[0][2][1])

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
                 
        
       # print(days[1])
        
