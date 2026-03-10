import copy
import random

class Hat:
    def __init__(self,**kwargs):

        self.contents = []
        for color,count in kwargs.items():
            self.contents.extend([color]*count)

    def draw(self,num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls_drawn)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_rate = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_count = {}

        for color in drawn_balls:
            drawn_count[color] = drawn_count.get(color,0) + 1

        success = True

        for color,count in expected_balls.items():
            if drawn_count.get(color,0) < count:
                success = False
                break

        if success:
            success_rate += 1

    return success_rate/num_experiments


