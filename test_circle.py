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

def test_circle_eq():
    c1=Circle(0,0,1)
    c2=Circle(1,1,1)
    assert c1==c2
    c3=Circle(0,0,2)
    assert c1 != c3

def test_circle_str():
    c = Circle(1,2,3)
    assert "Circle centered at" in str(c)

def test_circle_repr():
    c = Circle(1,2,3)
    assert "Circle" in repr(c)