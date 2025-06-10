#Exercise 1
print("\n")
#1 create an empty tuple
fruits = ()

#2 create a tuple with names of your siblings and brothers
sisters = ("haifa", "hanadi")
brothers = ("adnan",)

#3 create a new siblings tuple and join the earlier once
siblings = sisters + brothers

#4 how many siblings do you have
print(len(siblings))

#5 modify the siblings tuple and add your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append("ahmed")
siblings.append("rahma")
siblings = tuple(siblings)
family_members = siblings[0:]
print(family_members)
print(type(family_members))

#EXERCISE 2
#1 unpack siblings and parents
*siblings, father, mother = siblings
siblings = tuple(siblings)
parents = (father, mother)

