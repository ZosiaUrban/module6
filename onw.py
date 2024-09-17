import random
userinput=input(" Enter to roll ")

def roll():
 return random.randint(1,6)

rolled = 0

while rolled !=6:
 if userinput == "":
  rolled=roll()
 print(roll())
 print(f"you rolled {rolled}")
if roll == 6:
    print("You rolled a 6 you won!")

else:
 userinput=input(" Enter to roll ")