res = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

if "42" in res:
    print("Yes")
elif res.lower() == "forty-two" or res.lower() == "forty two":
    print("Yes")
else:
    print("No")

