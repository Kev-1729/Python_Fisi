import random


def main():
    r = get_level()

    for a in r:
        i = 0
        m = 0
        while True:
            while True:
                try:
                    clave = int(input(f"{a['x']} + {a['y']} = "))
                except ValueError:
                    print("EEE")
                else:
                    break

            if clave != a["res"]:
                print("EEE")
                m += 1
                if m == 3:
                    print(f"{a['x']} + {a['y']} = {a['res']}")
                    break
            else:
                i += 1
                break

    print(f"Score: {10-i}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= n <= 3:
                r = generate_integer(n)
                break
            else:
                pass
    return r


def generate_integer(level):
    r = []
    if level == 1:
        for _ in range(10):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            res = x + y

            p = {"x": x, "y": y, "res": res}
            r.append(p)
    else:
        for _ in range(10):
            x = random.randint(1 * 10 ** (level - 1), 10 ** (level))
            y = random.randint(1 * 10 ** (level - 1), 10 ** (level))
            res = x + y

            p = {"x": x, "y": y, "res": res}
            r.append(p)
    return r


if __name__ == "__main__":
    main()
