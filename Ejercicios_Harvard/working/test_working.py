from working import convert
import pytest

def main():
    test_hora_1()
    test_hora_2()
    test_hora_3()

def test_hora_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_hora_2():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_hora_3():
    with pytest.raises(ValueError):
        convert("161 AM to 12:PM")
    with pytest.raises(ValueError):
        convert("12-61 AM to 12-00 PM")
    with pytest.raises(ValueError):
        convert("12:61 AM to 12 PM")
    with pytest.raises(ValueError):
        convert("25 to 12 ")
    with pytest.raises(ValueError):
        convert("25 a 12")


if __name__ == "__main__":
    main()
