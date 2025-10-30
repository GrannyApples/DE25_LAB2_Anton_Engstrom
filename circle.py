from shape import Shape

PI = 3.141592

class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        ## super(). is used to link to the inheretor parent class(Shapes). this autocompleted first, so i had to google/llm what super does
        #and for different ways to do this, seems that super is the "best practice" according to AI.
        super().__init__(x, y)
        try:
            self.radius =float(radius)
        except:
            raise TypeError("must be a number")
        if self.radius <= 0:
            raise ValueError("radius aint positive")

    ##been to long since i used math like this, so i had to google the actual formulas.
    @property
    def area(self):
        return PI * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * PI * self.radius