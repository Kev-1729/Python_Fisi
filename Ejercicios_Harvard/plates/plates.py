def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 1
    num = 0
    if 2<= len(s) <= 6:
        for char in s:
            if i <= 2:
                if char.isnumeric():
                    return False

            if char.isnumeric():
                if num == 0 and char == "0":
                    return False
                num += 1

            if i + num != i:
                if not char.isnumeric():
                    return False

            i += 1
        return True
    else:
        return False


main()
