from rectangle import Rectangle
from pytest import raises

def test_rectangle_invalid_input():
    with raises(TypeError):
        Rectangle(0, 0, "a", 5)
    with raises(ValueError):
        Rectangle(0, 0, -2, 3)

def test_rectangle_area():
    r = Rectangle(0,0,2,4)
    assert r.area ==8

def test_rectangle_perim():
    r = Rectangle(0,0,2,4)
    assert r.perimeter==12

def test_rectangle_eq():
    r1 = Rectangle(0,0,2,4)
    r2 = Rectangle(1,1,2,4)
    assert r1==r2

##test to make sure width and height are the same to assert its a square...
def test_is_square():
    r = Rectangle(0, 0, 3, 3)
    assert r.is_square()