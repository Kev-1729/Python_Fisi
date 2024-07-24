def main():
    dic_frutas = [
        {"Fruta" : "Apple","Calorias": "130"},
        {"Fruta" : "Avocado","Calorias": "50"},
        {"Fruta" : "Banana","Calorias": "110"},
        {"Fruta" : "Cantaloupe","Calorias": "50"},
        {"Fruta" : "Grapefruit","Calorias": "60"},
        {"Fruta" : "Grapes","Calorias": "90"},
        {"Fruta" : "Honeydew Melon","Calorias": "50"},
        {"Fruta" : "Kiwifruit","Calorias": "90"},
        {"Fruta" : "Lemon","Calorias": "15"},
        {"Fruta" : "Lime","Calorias": "20"},
        {"Fruta" : "Nectarine","Calorias": "60"},
        {"Fruta" : "Orange","Calorias": "80"},
        {"Fruta" : "Peach","Calorias": "60"},
        {"Fruta" : "Pear","Calorias": "100"},
        {"Fruta" : "Pineapple","Calorias": "50"},
        {"Fruta" : "Plums","Calorias": "70"},
        {"Fruta" : "Strawberries","Calorias": "50"},
        {"Fruta" : "Sweet Cherries","Calorias": "100"},
        {"Fruta" : "Tangerine","Calorias": "50"},
        {"Fruta" : "Watermelon","Calorias": "80"},
    ]

    fruta = input("Item: ").title()
    for item in dic_frutas:
        if fruta in item["Fruta"]:
            print(f"Calories: {item["Calorias"]}")

main()
