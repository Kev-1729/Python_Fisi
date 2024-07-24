from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ")))


def validate(s):

    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
