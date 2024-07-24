import sys
import requests


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        try:
            n = float(sys.argv[1]) * 1.0
        except TypeError:
            sys.exit("Command-line argument is not a number")
        else:
            try:
                response = requests.get(
                    "https://api.coindesk.com/v1/bpi/currentprice.json"
                )
            except requests.RequestException:
                pass
            else:
                o = response.json()
                price = o["bpi"]["USD"]["rate_float"] * n
                print(f"${price:,.4f}")


if __name__ == "__main__":
    main()
