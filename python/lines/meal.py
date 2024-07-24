def main():
    time = input("what time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    hora, minuto = time.split(":")
    minuto = int(minuto)/60

    time = int(hora) + minuto
    return float(time)

if __name__ == "__main__":
    main()
