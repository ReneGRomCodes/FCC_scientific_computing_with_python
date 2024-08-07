# Encapsulation is a core OOP principle based on writing code that limits direct access to data.
# In this project, you'll discover new concepts related to encapsulation, such as getters, setters, and name mangling,
# and you'll use them together with what you already learned to create a program that calculates a projectile
# trajectory.
import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"


class Projectile:
    """Represents a projectile in motion."""

    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        """Initialize the projectile with speed, height, and angle."""
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)

    def __str__(self):
        """Return a string representation of the projectile's details."""
        return f'''
        Projectile details:
        speed: {self.speed} m/s
        height: {self.height} m
        angle: {self.angle}°
        displacement: {round(self.__calculate_displacement(), 1)} m
        '''

    def __calculate_displacement(self):
        """Calculate the horizontal displacement of the projectile."""
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component ** 2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)

        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    def __calculate_y_coordinate(self, x):
        """Calculate the y-coordinate for a given x-coordinate."""
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate

    def calculate_all_coordinates(self):
        """Calculate all (x, y) coordinates for the projectile's trajectory."""
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    @property
    def height(self):
        """Return the projectile's height."""
        return self.__height

    @property
    def angle(self):
        """Return the projectile's angle in degrees."""
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        """Return the projectile's speed."""
        return self.__speed

    @height.setter
    def height(self, n):
        """Set the projectile's height."""
        self.__height = n

    @angle.setter
    def angle(self, n):
        """Set the projectile's angle in degrees."""
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
        """Set the projectile's speed."""
        self.__speed = s

    def __repr__(self):
        """Return a string representation of the projectile."""
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'


class Graph:
    """Represents a graph of the projectile's trajectory."""

    __slots__ = ('__coordinates')

    def __init__(self, coord):
        """Initialize the graph with coordinates."""
        self.__coordinates = coord

    def __repr__(self):
        """Return a string representation of the graph."""
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        """Create a table of coordinates."""
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table

    def create_trajectory(self):
        """Create a visual representation of the projectile's trajectory."""

        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph


def projectile_helper(speed, height, angle):
    """Create a projectile, print its details, and show its trajectory."""
    # Create a Projectile instance with the given speed, height, and angle
    ball = Projectile(speed, height, angle)
    # Print the details of the projectile
    print(ball)
    # Calculate all coordinates for the projectile trajectory
    coordinates = ball.calculate_all_coordinates()
    # Create a Graph instance with the calculated coordinates
    graph = Graph(coordinates)
    # Print the table of coordinates
    print(graph.create_coordinates_table())
    # Print the graph of the trajectory
    print(graph.create_trajectory())


projectile_helper(10, 3, 45)
