class Rectangle:
    """
    Rectangle object
    """

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """
        Plot the rectangle on the canvas
        """
        canvas.array[self.x: self.x + self.width, self.y: self.y + self.height] = self.color


class Square:
    """
    Square object
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """
        Plot the square
        """
        canvas.array[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
