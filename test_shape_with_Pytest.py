from shape import Shape
from pytest import raises

def test_shape_init():
    s = Shape(1, 2)
    assert s.x == 1.0
    assert s.y == 2.0

def test_shape_typeerror():
    with raises(TypeError):
        Shape("a", 2)

def test_shape_repr():
    s = Shape(3, 4)
    assert "Shape" in repr(s)

def test_shape_str():
    s = Shape(3,4)
    assert "A Shape centered at" in str(s)