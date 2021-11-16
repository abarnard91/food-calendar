import random

#dinnerDict={"tacos":0, "burgers":1, "fish":2, "enchiladas":0}
#dinnerList=list(dinnerDict.keys())

#print(dinnerDict)
#print(dinnerList)
#print(random.choice(dinnerList))
#print(random.choice(list(dinnerDict.keys())))
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
dinnerDictlist=list(dinnerDict.keys())
print(dinnerDictlist)
dinnerTypePicker=random.randint(0,3)
if dinnerTypePicker == dinnerDictlist[0]:
    print("we're having mexican")
    dinner=random.choice(mexicanList)
    print(dinner)
if dinnerTypePicker == dinnerDictlist[1]:
    print("we're having grilled food")
    dinner=random.choice(grillList)
    print(dinner)
if dinnerTypePicker == dinnerDictlist[2]:
    print("we're having baked food")
    dinner=random.choice(bakedList)
    print(dinner)
if dinnerTypePicker == dinnerDictlist[3]:
    print("we're having italian food")
    dinner=random.choice(italianList)
    print(dinner)
