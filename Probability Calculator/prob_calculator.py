import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        balls_drawn = random.sample(self.contents, num_balls_drawn)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if balls_drawn.count(key) < value:
                success = False
                break
        if success:
            num_success += 1
    return num_success / num_experiments
