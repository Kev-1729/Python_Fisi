import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valor = re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", ip)
    if valor:
        for a in range(1, 5):
            if int(valor.group(a)) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()

link = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
