import random

class Die():

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1,self.sides))
        # sides = input("Is this a 10 or 20 sided die?")
        # if sides == 10:
        #     print("We'll use a 10 sided die.")
        #     sides = randint(1,10)
        # else:
        #     sides = randint(1,20)
        #     print("We'll use a 20-sided die.")


dice_roll = Die(20)

x = 1
while x < 10:
    dice_roll.roll_die()
    x += 1


# Pseudo Code
# - roll die needs to;
#     - print a random number between 1 and the number of side the die has
#       - need to be able to change how many sides the die has
#     - be able to roll each one 10 times
