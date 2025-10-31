from shape import Shape

class Rectangle(Shape):
    ##This autocompleted with intellisense, so just need to add height and width, will fix after circle is done.
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__(x, y)
        try:
            self.width = float(width)
            self.height = float(height)
        except:
            raise TypeError("width and height must be numbers")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("width and height must be positive")