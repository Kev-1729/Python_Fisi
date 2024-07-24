from seasons import minutos

def main():
    test_minutos_true()
    test_minutos_false()

def test_minutos_true():
    assert minutos("2000","10","11") == "Twelve million, two hundred nineteen thousand, eight hundred forty minutes"
    assert minutos("1980","10","11") == "Twenty-two million, seven hundred thirty-nine thousand forty minutes"

def test_minutos_false():
    assert minutos("10","11","2000") == "Invalid Date"

if __name__ == "__main__":
    main()
