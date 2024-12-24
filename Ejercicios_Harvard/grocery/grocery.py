def main():
    list = []
    cont = {}
    while True:
        try:
            item = input()
        except EOFError:
            break
        else:
            list.append(item)
    list.sort()
    list_upper = [item.upper() for item in list]
    for item in list_upper:
        if item in cont:
            cont[item] += 1
        else:
            cont[item] = 1

    for item, conteo in cont.items():

        print(f"{conteo} {item}")


main()
