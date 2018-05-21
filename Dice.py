""" Python Standard libarary functions"""

from random import randint

class Die():
    def __init__(self,sides):
        self.sides = sides

    def roll_dice(self):
        random_number_of_sides = randint(1,self.sides)
        print("You rolled a : " + str(random_number_of_sides))
     
dice = Die(6)
dice = Die(26)
dice.roll_dice()


dice = Die(66)
dice.roll_dice()

dice = Die(46)
dice.roll_dice()

dice = Die(123346)
dice.roll_dice()
