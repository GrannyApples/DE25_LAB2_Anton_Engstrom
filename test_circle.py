from pytest import raises
from circle import Circle

def test_circle_invalid_radius():
    with raises(TypeError):
        Circle(0, 0, "abc")
    with raises(ValueError):
        Circle(0, 0, -5)