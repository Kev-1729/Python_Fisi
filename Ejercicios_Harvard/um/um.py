import re


def main():
    print(count(input("Text: ")))


def count(s):
    contar = re.findall(r"\b[(um)]{2}\b", s, re.IGNORECASE)
    return len(contar)


if __name__ == "__main__":
    main()
