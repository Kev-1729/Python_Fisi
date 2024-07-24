import random


def main():
    a = 0
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n < 1:
                continue
            else:
                break

    number = random.randint(1, n)

    while number != a:
        try:
            a = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if n < a:
                continue
            else:
                if a < number:
                    print("Too small!")
                elif a > number:
                    print("Too large!")
                else:
                    print("Just right!")


if __name__ == "__main__":
    main()
