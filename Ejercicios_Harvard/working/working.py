import re



def main():
    print(convert(input("Hours: ")))


def convert(s):
    hora = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)

    if hora:
        if hora.group(2):
            if int(hora.group(2)) >= 60:
                raise ValueError
        if hora.group(5):
            if int(hora.group(5)) >= 60:
                raise ValueError

        hora1 = int(hora.group(1))
        if hora.group(3) == "PM":
            hora1 += 12
            if hora1-12 == 12:
                hora1 = 12
        elif hora.group(3) == "AM" and hora1 == 12:
            hora1 -= 12
        if hora.group(2) == None:
            time = f"{hora1:02}:00"
        else:
            time = f"{hora1:02}:{hora.group(2)}"

        hora2 = int(hora.group(4))
        if hora.group(6) == "PM":
            hora2 += 12
            if hora2-12 == 12:
                hora2 = 12
        elif hora.group(6) == "AM" and hora2 == 12:
            hora2 -= 12
        if hora.group(5) == None:
            time2 = f"{hora2:02}:00"
        else:
            time2 = f"{hora2:02}:{hora.group(5)}"

        a = f"{time} to {time2}"
        return a
    else:
        raise ValueError

if __name__ == "__main__":
    main()
