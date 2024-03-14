import copy
import random


class Hat:

    def __init__(self, **colors):
        self.colors = colors
        self.contents = [k for k, v in self.colors.items() for _ in range(v)]

    def draw(self, n):
        pass


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


# Instance, method and function calls to test functionality and outputs.
test_hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
