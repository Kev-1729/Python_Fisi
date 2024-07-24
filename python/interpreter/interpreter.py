x, y, z = input("expression: ").split(" ")

if y == "+":
    res = float(int(x) + int(z))
    print(f"{res:.1f}")
elif y == "-":
    res = float(int(x) - int(z))
    print(f"{res:.1f}")
elif y == "*":
    res = float(int(x) * int(z))
    print(f"{res:.1f}")
elif y == "/":
    res = float(int(x) / int(z))
    print(f"{res:.1f}")
