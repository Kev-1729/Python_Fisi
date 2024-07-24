from numb3rs import validate


def main():
    test_validate_true()
    test_validate_false()


def test_validate_true():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_validate_false():
    assert validate("1100.2.3.10") == False
    assert validate("1.555.555.555") == False
    assert validate("cat") == False


if __name__ == "__main__":
    main()
