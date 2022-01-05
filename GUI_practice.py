from tkinter import *
from PIL import ImageTk, Image
#import monthly_dinner_calendar as MDC


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

#monthImage=Label(window, text=((MDC.presentMonth +" "+ str(MDC.presentYear))), font=("Arial", 40), anchor=CENTER, background="white")
monthImage=Label(window, text=("December 2021"), font=("Arial", 40), anchor=CENTER, background="white")
#monthImage.size("458x70")
monthImage.pack()
#creates the "label" monthImage on top of the canvas (the calendar jpeg)
canvas.create_window(512,93, window=monthImage)

x=170
y=166
counter=0

def calendarDateNumber(date, x, y):
    date=Label(window, text=(str(date)), font=("Arial",14), anchor=CENTER, background="white")
    date.pack()
    canvas.create_window(x, y, window=date)
    
    

##numberOne=Label(window, text=1, font=("Arial",14), anchor=CENTER, background="white")
##numberOne.pack()
##
##numberTwo=Label(window, text="2", font=("Arial",14), anchor=CENTER, background="white")
##canvas.create_window(170,166, window=numberOne)
##canvas.create_window(300,166, window=numberTwo)
aList=[1,2,3,4,5,6,7,8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
for i in aList:
    #print(i)
    calendarDateNumber(i,x,y)
    x+=130
    counter+=1
    if counter>6:
        y+=121
        x=170
        counter=0
        
salsaChicken=Label(window, text="Salsa Chicken", font=("Arial",10), anchor=CENTER, background="white")
salsaChicken.pack()
canvas.create_window(120,210,window=salsaChicken)

turkeyTaco=Label(window, text="Turkey Tacos", font=("Arial",10), anchor=CENTER, background="white")
turkeyTaco.pack()
canvas.create_window(250,210,window=turkeyTaco)

###Add image as a PNG w/o using PIL and ImageTK
##img =PhotoImage(file="blank calendar.png")
##
##Label(window, image=img, anchor=CENTER).pack()
##

window.mainloop()
