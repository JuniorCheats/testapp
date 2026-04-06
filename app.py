python
def add(a,b):
    return a+b

def test_add():
    assert add(2,2)==4
Файл test_app.py:
from app import add

def test_add_positive():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, -1) == -2
