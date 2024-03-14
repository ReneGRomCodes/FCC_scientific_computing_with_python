import copy
import random


class Hat:
    """Represent a hat filled with balls of different colors."""

    def __init__(self, **colors):
        """Initialize a Hat object with variable key-value pairs representing balls of different colors in dict
        'self.colors' and a list 'self.contents' containing all the balls separately."""
        self.colors = colors
        self.contents = [k for k, v in self.colors.items() for _ in range(v)]

    def draw(self, n):
        """Draw amount 'n' of balls from hat 'self.contents', pop them from list, then add them to and return new list
        'drawn_balls'. If 'n' exceeds amount of items in 'self.contents', all balls are returned."""
        drawn_balls = []
        if n <= len(self.contents):
            for i in range(n):
                drawn_ball = self.contents.pop(random.choice(range(len(self.contents))))
                drawn_balls.append(drawn_ball)
        else:
            drawn_balls = self.contents

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


# Instance, method and function calls to test functionality and outputs.
test_hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(test_hat.contents)
print(test_hat.draw(50))
print(test_hat.draw(5))
print(test_hat.contents)
