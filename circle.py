from shape import Shape

PI = 3.141592

class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        try:
            self.radius =float(radius)
        except:
            raise TypeError("must be a number")
        if self.radius <= 0:
            raise ValueError("radius aint positive")
