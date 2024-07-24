from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("1/100") == 1
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cata/1")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

if __name__ == "__main__":
    main()
