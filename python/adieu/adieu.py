def main():
    list = []
    while True:
        try:
            item = input("Name: ")
        except EOFError:
            break
        else:
            list.append(item)

    print("Adieu, adieu, to ",end="")

    # Liesl
    # Liesl and Friedrich
    # Liesl, Friedrich, and Louisa
    # Liesl, Friedrich, Louisa, and Kurt

    if len(list) == 1:
        print(list[0])

    elif len(list) == 2:
        print(list[0]+" and "+list[1])

    for name in list:
        if len(list)>2:
            if name == list[len(list)-1]:
                print(f"and {name}")
            else:
                print(f"{name}, ",end="")
        else:
            break


if __name__ == "__main__":
    main()
