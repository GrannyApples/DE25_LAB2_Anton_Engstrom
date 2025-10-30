class Shape:
    def __init__(self,x=0, y=0):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            raise TypeError("X and Y must be numbers")