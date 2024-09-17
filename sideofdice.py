import random


def roll(sides):
    return random.randint(1, sides)


sides = int(input("Enter the number of sides: "))
rolled = 0


while rolled != sides:

    userinput = input("Press Enter to roll the dice or type 'exit' to quit: ")


    if userinput.lower() == "exit":
        print("Exiting the program.")
        break

    if userinput == "":
        rolled = roll(sides)
        print(f"You rolled: {rolled}")


        if rolled == sides:
            print(f"You rolled the maximum number {sides}! You won!")
