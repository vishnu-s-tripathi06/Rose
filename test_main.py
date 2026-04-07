from main import Square
from Car import hello



def test_positive():
    assert Square(8)==64

    assert Square(3)==9

def test_negative():
    assert Square(-3) == 9
def test_zero():
    assert Square(0) == 0

def test_hello():
    assert hello() == "Hello World"







