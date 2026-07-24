from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])

        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

          
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


# 15.4 
#  I made it longer 0 to 8 and result: Bigger steps that covers a bigger area
# I changed x_direction = choice([1]) and the result was : It can only move to the right