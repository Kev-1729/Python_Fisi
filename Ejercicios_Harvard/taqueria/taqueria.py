def main():
    dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    n = 0
    while True:
        try:
            item = input("Item: ").lower().title()
        except EOFError:
            break
        else:
            if item in dict:
                n += dict.get(item)
                print(f"Total: ${n:.2f}")
            else:
                pass


if __name__ == "__main__":
    main()
