import random

#dinnerDict={"tacos":0, "burgers":1, "fish":2, "enchiladas":0}
#dinnerList=list(dinnerDict.keys())

#print(dinnerDict)
#print(dinnerList)
#print(random.choice(dinnerList))
#print(random.choice(list(dinnerDict.keys())))
dinnerDict={0:"mexican", 1:"grill", 2:"baked"}
mexicanList=["tacos", "enchiladas"]
grillList=["burger","brats"]
bakedList=["fish","chicken"]
dinnerDictlist=list(dinnerDict.keys())
print(dinnerDictlist)
dinnerTypePicker=random.randint(0,2)
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
