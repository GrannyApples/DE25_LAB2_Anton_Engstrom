from shape import Shape

class Rectangle(Shape):
    """A rectangle defined by its center (x, y), width, and height."""
    ##This autocompleted with intellisense, so just need to add height and width, will fix after circle is done.
    def __init__(self, x:float=0, y:float=0, width:float=1, height:float=1) -> None:
        super().__init__(x, y)
        try:
            self.width = float(width)
            self.height = float(height)
        except:
            raise TypeError("width and height must be numbers")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("width and height must be positive")
        
    ##Again used LLM just for the math formula. 
    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width+self.height)
    
    def __repr__(self):
        return f"Rectangle (x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    def __str__(self):
        return f"Rectangle centered at (x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return self.width == self.height
