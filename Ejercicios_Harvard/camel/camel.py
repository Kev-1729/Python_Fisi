def main():

    camel = input("camelCase: ")
    snake_case = ""

    #holaHola = hola_hola
    #HOla_hOLA

    for _ in camel:
        if _ == _.upper():
            snake_case += "_" + _.lower()
        else:
            snake_case += _

    print("snake_case:", snake_case)

main()
