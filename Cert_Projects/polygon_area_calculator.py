class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        s = f"Rectangle(width={self.width}, height={self.height})"
        return s

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        pass

    def get_amount_inside(self, other_shape):
        pass


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        s = f"Square(side={self.side})"
        return s

    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side


# Instance, method and function calls to test functionality and outputs.
rect = Rectangle(10, 5)
sqr = Square(7)
print(rect)
print(sqr)
