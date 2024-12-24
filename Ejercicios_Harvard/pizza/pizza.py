import sys
from tabulate import tabulate
import csv

def main():
    pizza = []
    headers = {}
    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        if ".csv" in sys.argv[1]:
            try:
                with open(f"{archivo}") as file:
                    reader = csv.reader(file)

                    headers = next(reader)

                    for row in reader:
                        pizza.append(row)

                    print(tabulate(pizza, headers, tablefmt="grid"))

            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CVS file")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        print("Too many command-line arguments")

if __name__ == "__main__":
    main()
