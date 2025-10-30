from pytest import raises
from circle import Circle

def test_circle_invalid_radius():
    with raises(TypeError):
        Circle(0, 0, "abc")
    with raises(ValueError):
        Circle(0, 0, -5)

##just used a calc to get the correct == cant do that math in my head.
def test_circle_area():
    c = Circle(0,0,2)
    assert round(c.area,2)==12.57

def test_circle_perim():
    c=Circle(0,0,2)
    assert round(c.perimeter, 2)==12.57