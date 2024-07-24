import sys


def main():
    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        i = 0
        if ".py" in sys.argv[1]:
            try:
                with open(f"{archivo}", "r") as file:
                    for line in file:
                        line = line.strip()
                        if line.startswith("#"):
                            pass
                        elif not line:
                            pass
                        else:
                            i += 1
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")
    else:
        print("Too few command-line arguments")

    print(i)


if __name__ == "__main__":
    main()
