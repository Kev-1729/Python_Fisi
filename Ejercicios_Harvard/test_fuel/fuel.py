def main():
    f = input("Fraction: ")
    por = convert(f)
    print(gauge(por))


def convert(fraction):
    while True:
        x, y = fraction.split("/")
        try:
            x = int(x)
            y = int(y)
            por = round(x * 100 / y)
            if x > y:
                fraction = input("Fraction: ")
                continue
            else:
                return por
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
