from random import randint

class Die:

    #single die class

    def __init__(self, num_sides=6):
        
        self.num_sides = num_sides

    def roll(self):

        #return random value between 1 and 6
        return randint(1, self.num_sides)    