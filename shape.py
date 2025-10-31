class Shape:
    """Base class for all shapes.

    Handles x/y position, translation, and comparison between shapes
    based on their area.
    """
    def __init__(self,x=0, y=0):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            raise TypeError("X and Y must be numbers")
    
    def __repr__(self):
        return f"Shape(x={self.x}, y={self.y})"

    def __str__(self):
        return f"A Shape centered at ({self.x}, {self.y})"
    
    def translate(self, dx, dy):
        try:
            self.x += float(dx)
            self.y += float(dy)
        except:
            raise TypeError("dx and dy must be numbers")
        
    ## went back and forth with an LLM to figure out just how to write all the operation overflows
    # for this... from what i understand, its needed to change the default behaviour where python checks memory allocation 
    # to instead check for value instead. 
        
    def __eq__(self, other):
        try:
            return self.area == other.area
        except AttributeError as e:
            print(f"not equal returns false, error:{e}")
            return False

    def __lt__(self, other):
        try:
            return self.area < other.area
        except AttributeError as e:
            raise TypeError(f"Can only compare shapes. Error: {e}")

    def __le__(self, other):
        try:
            return self == other or self < other
        except AttributeError as e:
            raise TypeError(f"Can only compare shapes. Error: {e}")

    def __gt__(self, other):
        try:
            return self.area > other.area
        except AttributeError as e:
            raise TypeError(f"Can only compare shapes. Error: {e}")

    def __ge__(self, other):
        try:
            return self == other or self > other
        except AttributeError as e:
            raise TypeError(f"Can only compare shapes. Error: {e}")