import re

def main():
    print(parse(input("HTML: ")))



def parse(s):
    link = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if link:
        you = "https://youtu.be/" + link.group(1)
        return you
    elif link == None:
        return None
    else:
        return False


if __name__ == "__main__":
    main()
