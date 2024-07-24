import sys
from PIL import Image, ImageOps, ImageFilter


def main():
    if len(sys.argv) == 3:
        if (
            ".png" in sys.argv[1].lower()
            or ".jpeg" in sys.argv[1].lower()
            or ".jpg" in sys.argv[1].lower()
        ):
            if (
                ".png" in sys.argv[2].lower()
                or ".jpeg" in sys.argv[2].lower()
                or ".jpg" in sys.argv[2].lower()
            ):
                if sys.argv[1][-4:] == sys.argv[2][-4:]:

                    image_1 = Image.open(sys.argv[1])
                    shirt = Image.open("shirt.png")
                    size = shirt.size
                    img = ImageOps.fit(image_1,size)
                    img.paste(shirt, shirt)
                    img.save(sys.argv[2])
                else:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
        else:
            sys.exit("Input and output have different extensions")
    elif len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
