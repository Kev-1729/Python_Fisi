import sys
import csv

def main():
    students = []
    nuevo_diccionario = {}
    if len(sys.argv) == 3:
        if "before.csv" == sys.argv[1] or ".csv" in sys.argv[1]:
            with open(sys.argv[1], newline="") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    students.append({"name": row[0], "home": row[1]})

                for index, valor in enumerate(students):
                    nuevo_diccionario[index] = valor["name"].split(", ")

        else:
            sys.exit(f"Could not write to {sys.argv[1]}")

        if ".csv" in sys.argv[2]:
            with open(sys.argv[2], "w", newline="") as file:
                reader_1 = csv.writer(file)
                reader_1.writerow(["first", "last", "house"])

                for index, palabra in nuevo_diccionario.items():
                    reader_1.writerow([palabra[1], palabra[0], students[index]["home"]])

        else:
            sys.exit(f"Could not write to {sys.argv[2]}")

    elif len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")
    else:
        print("Too many command-line arguments")


if __name__ == "__main__":
    main()
