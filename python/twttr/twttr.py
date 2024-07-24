def main():

    text = input("Input: ")
    new_text = shorten(text)
    print(f"Output: {new_text}")

def shorten(word):

    lista_vocales = ["a","e","i","o","u"]
    new_text = ""
    for char in word:
        if char.lower() in lista_vocales:
            pass
        else:
            new_text += char

    return new_text

if __name__ == "__main__":
    main()
