import emoji

def main():

    text = input("Input: ").split(" ")
    text_emoji = ""


    for _ in text:
            text_emoji += emoji.emojize(_, language="alias") + " "

    print(f"Output: {text_emoji.strip()}")


if __name__ == "__main__":
    main()
