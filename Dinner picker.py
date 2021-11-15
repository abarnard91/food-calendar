
#finish sides lists for dinner types 2-4





import keyboard
import random

areYouDone=False
isThisTheDay = False



#dinner list
dinnerDict={"Hamburgers":1,
            "Tacos":2,
            "Brats":1,
            "Pizza":5,
            "Grilled Chicken thighs":1,
            "Orange Chicken":0,
            "Salsa Chicken":2,
            "Chili":4,
            "Sloppy Joes":1,
            "Pulled Chicken":1,
            "Pulled Pork":1,
            "Pasta":3,
            "Enchiladas":2,
            "Order out":0,
            "Baked Mastaccioli":3,
            "grilled chicken wings":1,
            "mexican stuffed peppers":2,
            "Quiche loraine":0,
            "crockpot chicken":6,
            "Cauliflower pizza":6,
            "Ramen noodle stirfry":0,
            "left overs":0,
            "English muffin pizza":0,
            "Loaded baked potato":6}

dinnerList=["Hamburgers",
            "Tacos",
            "Brats",
            "Pizza",
            "Grilled Chicken thighs",
            "Orange Chicken",
            "Salsa Chicken",
            "Chili",
            "Sloppy Joes",
            "Pulled Chicken",
            "Pulled Pork",
            "Pasta",
            "Enchiladas",
            "Order out",
            "Baked Mastaccioli",
            "grilled chicken wings",
            "mexican stuffed peppers",
            "Quiche loraine",
            "crockpot chicken",
            "Cauliflower pizza",
            "Ramen noodle stirfry",
            "left overs",
            "English muffin pizza",
            "Loaded baked potato"
            ]
#1
grilledSideList=["Seasoned fries",
                 "Sweet potato fries",
                 "Baked Beans",
                 "Mac n Cheese",
                 "Potato Salad",
                 "Pasta Salad",
                 "No side"]

#6
vegetableSideList=["Corn",
                   "Broccoli",
                   "Peas",
                   "Green Beans",
                   "zucchini",
                   "Carrots",
                   "Salad mix",
                   "No vegetable side"]

#2
mexicanSideList=["Refried Beans",
                 "Rice",
                 "guacamole",
                 "Chips",
                 "Elote",
                 "No side"]
#3
pastaSideList=["Salad mix",
               "Garlic bread",
               "No side"]

#4
pizzaSideList=["Salad mix",
           "Wings",
           "No side"]

#5
chiliSideList=["Corn bread",
           "No side"]

dinnerBackUpList=[]
sideBackUpList=[]
vegetableBackUpList=[]

                   
          
def pickDinner():
    global dinnerList
    goodChoice= False
    print ("Great let's see what's for dinner!")
    while goodChoice == False:

        if not dinnerList:
            endOfDinnerListResponse=input(("You reached the end of the list! Do you want to try again? (yes or no)"))

            if endOfDinnerListResponse == "yes":
                dinnerList.extend(dinnerBackUpList)
                dinnerBackUpList.clear()
                
            else:
                print("OK")
                killProgram()
        else:

            dinnerChoice=random.choice(dinnerList)
            print(dinnerChoice + " for dinner tonight!")
            soundsGood=input("Does that sound good? (enter yes or no)")
            if soundsGood == "yes":
                sidePicker=dinnerDict.get(dinnerChoice)

                
                dinnerSideFunction=False

                while dinnerSideFunction==False:
                    vegetableLoop= False
                    if sidePicker == 0:
                        dinnerSideFunction=True

                    if sidePicker == 1:
                        print("Let's pick some sides for the grill!")

                        if not grilledSideList:
                            endOfGrilledSideListResponse=input(("You've run out of side options! do you want to pick side again? (yes or no)"))
                            if endOfGrilledSideListResponse == "yes":
                                grilledSideList.extend(sideBackUpList)
                                sideBackUpList.clear()
                            else:
                            
                                dinnerSideFunction=True
                                break
                            
                            
                        else:
                            sideChoice=random.choice(grilledSideList)
                            sideApproval=input(sideChoice +" Does that sound good? (Enter yes or no)")
                            if sideApproval == "yes":
                                print ("Awesome time for a vegetable")
                                while vegetableLoop == False:
                                    if not vegetableSideList:
                                        endOfVegetableSideListResponse=input(("You've run out of vegi side options! do you want to pick side again? (yes or no)"))
                                        if endOfVegetableSideListResponse == "yes":
                                            vegetableSideList.extend(vegetableBackUpList)
                                            vegetableBackUpList.clear()
                                        else:
                                        
                                            dinnerSideFunction=True
                                            break

                                    else:                                
                                        sideChoiceTwo=random.choice(vegetableSideList)
                                        sideApprovalTwo= input(sideChoiceTwo + " Does that sound good? (Enter yes or no)")
                                    
                                        if sideApprovalTwo == "yes":
                                            print ("Awesome")
                                            vegetableLoop= True
                                            dinnerSideFunction=True
                                            break
                                        else:
                                            vegetableBackUpList.append(sideChoiceTwo)
                                            vegetableSideList.remove(sideChoiceTwo)
                                            print("Ok let's try again")
                                            dinnerSideFunction=True
                            else:
                                sideBackUpList.append(sideChoice)
                                grilledSideList.remove(sideChoice)
                                print("Ok let's try again")


                        
                    if sidePicker == 2:
                        print("Let's pick a side for this mexican fiesta!")
                        if not mexicanSideList:
                            endOfMexicanSideListResponse=input(("You've run out of side options! do you want to pick side again? (yes or no)"))
                            
                            if endOfMexicanSideListResponse == "yes":
                                mexicanSideList.extend(sideBackUpList)
                                sideBackUpList.clear()
                            else:
                            
                                dinnerSideFunction=True
                                break
                            
                        else:
                            sideChoice=random.choice(mexicanSideList)
                            sideApproval=input(sideChoice +" Does that sound good? (Enter yes or no)")
                            if sideApproval == "yes":
                                print ("Awesome")
                                dinnerSideFunction=True
                            else:
                                print("Ok let's try again")
                                sideBackUpList.append(sideChoice)
                                mexicanSideList.remove(sideChoice)




                        
                    if sidePicker == 3:
                        print("Let's smash like Mario! Let's pick an italian side!")
                        if not pastaSideList:
                            endOfPastaSideListResponse=input(("You've run out of side options! do you want to pick side again? (yes or no)"))
                            
                            if endOfPastaSideListResponse == "yes":
                                pastaSideList.extend(sideBackUpList)
                                sideBackUpList.clear()
                            else:
                            
                                dinnerSideFunction=True
                                break
                            
                        else:
                            sideChoice=random.choice(pastaSideList)
                            sideApproval=input(sideChoice +" Does that sound good? (Enter yes or no)")
                            if sideApproval == "yes":
                                print ("Awesome")
                                dinnerSideFunction=True
                            else:
                                print("Ok let's try again")
                                sideBackUpList.append(sideChoice)
                                pastaSideList.remove(sideChoice)



                                
                    if sidePicker == 4:
                        print("Alright! Chili night!!! You want a side? It's a short list")
                        if not chiliSideList:
                            endOfChiliSideListResponse=input(("You've run out of side options! do you want to pick side again? (yes or no)"))
                            
                            if endOfChiliSideListResponse == "yes":
                                chiliSideList.extend(sideBackUpList)
                                sideBackUpList.clear()
                            else:
                            
                                dinnerSideFunction=True
                                break
                            
                        else:
                            sideChoice=random.choice(chiliSideList)
                            sideApproval=input(sideChoice +" Does that sound good? (Enter yes or no)")
                            if sideApproval == "yes":
                                print ("Awesome")
                                dinnerSideFunction=True
                            else:
                                print("Ok let's try again")
                                sideBackUpList.append(sideChoice)
                                chiliSideList.remove(sideChoice)


                                

                        
                    if sidePicker == 5:
                        print("Let's pick a side for pizza!")
                        if not pizzaSideList:
                            endOfPizzaSideListResponse=input(("You've run out of side options! do you want to pick side again? (yes or no)"))
                            
                            if endOfPizzaSideListResponse == "yes":
                                pizzaSideList.extend(sideBackUpList)
                                sideBackUpList.clear()
                            else:
                            
                                dinnerSideFunction=True
                                break
                            
                        else:
                            sideChoice=random.choice(pizzaSideList)
                            sideApproval=input(sideChoice +" Does that sound good? (Enter yes or no)")
                            if sideApproval == "yes":
                                print ("Awesome")
                                dinnerSideFunction=True
                            else:
                                print("Ok let's try again")
                                sideBackUpList.append(sideChoice)
                                pizzaSideList.remove(sideChoice)

                    if sidePicker == 6:
                        while vegetableLoop == False:
                                    if not vegetableSideList:
                                        endOfVegetableSideListResponse=input(("You've run out of vegi side options! do you want to pick side again? (yes or no)"))
                                        if endOfVegetableSideListResponse == "yes":
                                            vegetableSideList.extend(vegetableBackUpList)
                                            vegetableBackUpList.clear()
                                        else:
                                        
                                            dinnerSideFunction=True
                                            break

                                    else:                                
                                        sideChoice=random.choice(vegetableSideList)
                                        sideApproval= input(sideChoice + " Does that sound good? (Enter yes or no)")
                                    
                                        if sideApproval == "yes":
                                            print ("Awesome")
                                            vegetableLoop= True
                                            dinnerSideFunction=True
                                            break
                                        else:
                                            vegetableBackUpList.append(sideChoice)
                                            vegetableSideList.remove(sideChoice)
                                            print("Ok let's try again")
                                            dinnerSideFunction=True
                            
                            
                    isThisTheDay = True
                    goodChoice=True
                
            else:
                print ("Ok, let's try something different.")
                dinnerBackUpList.append(dinnerChoice)
                dinnerList.remove(dinnerChoice)
            
    
        

def killProgram():
    print ("press enter to exit")
    keyboard.wait("enter")
    areYouDone=True 
    exit()


def restartProgram():
    backToTheBeginning=input("Do you want to pick a different day? (yes or no)")
    if backToTheBeginning== "no":
        killProgram()
    else:
        isThisTheDay= False
        doYouWantDinner=backToTheBeginning

    

while areYouDone == False:
    doYouWantDinner = input("Do you want me to pick dinner for the week? (yes or no)")
    
    if doYouWantDinner == "yes":
        print( "Ok! Let's do it")
        while isThisTheDay == False:
            dayOfTheWeek= (input("What day is it? (1=Monday, 2= Tuesday, 3=Wednesday 4= Thursday 5=Friday 6=Saturday, 7=Sunday)(Enter just the number)"))
            
            if dayOfTheWeek == "1":
                dayConfirmation=input ("Are you sure Monday is the correct day (enter yes or no)")

                if dayConfirmation== "yes":

                    pickDinner()
                    restartProgram()
                    
                    
                    break
                    
                else:
                    print("Ok, let's try this again")
                    
            if dayOfTheWeek == "2":
                dayConfirmation=input ("Are you sure Tuesday is the correct day (enter yes or no)")

                if dayConfirmation== "yes":
                    pickDinner()
                    restartProgram()
                    break
                else:
                    print("Ok, let's try this again")
                    
            if dayOfTheWeek == "3":
                dayConfirmation=input ("Are you sure Wednesday is the correct day (enter yes or no)")

                if dayConfirmation== "yes":
                    pickDinner()
                    restartProgram()
                    break
                else:
                    print("Ok, let's try this again")

            if dayOfTheWeek == "4":
                dayConfirmation=input ("Are you sure Thursday is the correct day (enter yes or no)")

                if dayConfirmation== "yes":
                    pickDinner()
                    restartProgram()
                    break
                
                else:
                    print("Ok, let's try this again")

            if dayOfTheWeek == "5":
                dayConfirmation=input ("Are you sure Friday is the correct day (enter yes or no)")

                if dayConfirmation== "yes":
                   pickDinner()
                   restartProgram()
                   break
                else:
                    print("Ok, let's try this again")

            if dayOfTheWeek == "6":
                dayConfirmation=input ("Are you sure Saturday is the correct day (enter yes or no)")

                if dayConfirmation== "yes":
                    pickDinner()
                    restartProgram()
                    break
                else:
                    print("Ok, let's try this again")

            if dayOfTheWeek == "7":
                dayConfirmation=input ("Are you sure Sunday is the correct day (enter yes or no)")

                if dayConfirmation== "yes":
                    pickDinner()
                    restartProgram()
                    break

                else:
                    print("Ok, let's try this again")

            else:
                  print(" Please enter 1,2,3,4,5,6, or 7")  
                       
        
    
    if doYouWantDinner == "no":
        print ("Ok, maybe later")
        killProgram()
        break

    else:
        print ("try again. Enter yes or no")




    
