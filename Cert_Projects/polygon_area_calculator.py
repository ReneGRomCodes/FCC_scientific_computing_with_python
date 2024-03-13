class Rectangle:
    """Represent geometric shape of a rectangle."""

    def __init__(self, width, height):
        """Initialize width and height attributes."""
        self.width = width
        self.height = height

    def __str__(self):
        """Return formatted string containing width and height."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        """Set new width."""
        if new_width <= 0:
            print("Width cannot be negative or 0.")
            return
        self.width = new_width

    def set_height(self, new_height):
        """Set new height."""
        if new_height <= 0:
            print("Height cannot be negative or 0.")
            return
        self.height = new_height

    def get_area(self):
        """Calculate and return area of instance."""
        return self.width * self.height

    def get_perimeter(self):
        """Calculate and return perimeter of instance."""
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        """Calculate and return diagonal of instance."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Create string visually representing the instance if width or height do no exceed 50."""
        # Check if height or width of rectangle exceeds value of 50 and return string if 'True'
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        # Assign empty variable 'picture', create visual representation of rectangle using '*'s, assign them to and
        # return 'picture'.
        picture = ""
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, other_shape):
        """Take instance 'other_shape' and return the number of times the passed in shape could fit inside the shape
        (with no rotations)"""
        if other_shape.width > self.width or other_shape.height > self.height:
            return 0
        else:
            height_inside = self.height // other_shape.height
            width_inside = self.width // other_shape.width
            return height_inside * width_inside


class Square(Rectangle):
    """Represent geometric shape of a square as a special case of a rectangle."""

    def __init__(self, side):
        """Initialize side, width and height attributes. Width and height equal side for a square."""
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        """Return formatted string containing width and height."""
        return f"Square(side={self.side})"

    def set_side(self, new_side):
        """Set new side length. Assign same value to width and height."""
        if new_side <= 0:
            print("Length of side cannot be negative or 0.")
            return
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        """Set new width. Assign same value to height and side."""
        super().set_width(new_width)
        self.side = new_width
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        """Set new height. Assign same value to width and side."""
        super().set_height(new_height)
        self.side = new_height
        self.width = new_height
        self.height = new_height


# Instance, method and function calls to test functionality and outputs.
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
