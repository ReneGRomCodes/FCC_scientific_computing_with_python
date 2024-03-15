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
    """Simulate drawing balls from a hat and calculate the probability of drawing a specific combination of balls.
        Args:
            hat (Hat): An instance of the Hat class representing the hat containing balls.
            expected_balls (dict): A dictionary representing the expected counts of each color of ball to be drawn.
            num_balls_drawn (int): The number of balls to be drawn from the hat in each experiment.
            num_experiments (int): The number of experiments to be conducted.
        Returns the probability of drawing the expected combination of balls as a float."""
    # Initialize counters for experiments where the expected combination is drawn.
    exp_counter = 0
    true_counter = 0
    # Iterate over the number of experiments.
    while exp_counter < num_experiments:
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls contain at least the expected counts.
        contains_enough = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                contains_enough = False
                break  # No need to continue checking if one color is insufficient.
        # If the drawn balls contain at least the expected counts, increment the true_counter.
        if contains_enough:
            true_counter += 1

        exp_counter += 1

    # Calculate and return the probability of drawing the expected combination of balls.
    return true_counter / num_experiments


# Instance and function calls to test functionality and outputs.
test_hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=test_hat,
                  expected_balls={"red": 2, "green": 1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
