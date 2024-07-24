from pyfiglet import Figlet
import sys
from random import choice


def main():
    figlet = Figlet()
    list_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        text = input("Input: ")
        fuente = choice(list_fonts)
        figlet.setFont(font=fuente)
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        else:
            fuente = sys.argv[2]
            if fuente in list_fonts:
                text = input("Input: ")
                figlet.setFont(font=fuente)
                print(figlet.renderText(text))
            else:
                sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
