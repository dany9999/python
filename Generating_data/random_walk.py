""" In this section, we’ll use Python to generate data for a random walk, and then use Matplotlib to create a visually appealing representation of that
data. A random walk is a path that has no clear direction but is determined by a series of random decisions, each of which is left entirely to chance. You
might imagine a random walk as the path a confused ant would take if it took every step in a random direction.

Random walks have practical applications in nature, physics, biology, chemistry, and economics. For example, a pollen grain floating on a
drop of water moves across the surface of the water because it’s constantly pushed around by water molecules. Molecular motion in a water drop is
random, so the path a pollen grain traces on the surface is a random walk. The code we’ll write next models many real-world situations. """

from random import choice

class RandomWalk:
    
    #a class to generate random walks

    def __init__(self, num_points=5000):
        
        #initialize attributes of a walk
        self.num_points = num_points

        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):

        #calculate all the the points in the walk

        #keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            #decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)    