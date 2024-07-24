def main():
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
        except ValueError:
            continue
        else:
            if x <= y:
                try:
                    por = round(x*100/y)
                except ZeroDivisionError:
                    continue
                else:
                    if por >= 99:
                        print("F")
                    elif por <= 1 :
                        print("E")
                    else:
                        print(f"{por}%")
            else:
                continue
            break
main()
