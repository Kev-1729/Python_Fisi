from datetime import date
import sys
import inflect

a = inflect.engine()

def main():
    try:
        anio, mes, dia = input("Date of Birth: ").split("-")

    except ValueError:
        sys.exit("Invalid Date")

    print(minutos(anio, mes, dia))


def minutos(anio, mes, dia):
    try:
        fecha = date(int(anio), int(mes), int(dia))
    except ValueError:
        return "Invalid Date"

    hoy = date.today()
    min = int((hoy - fecha).total_seconds()/60)
    texto = (a.number_to_words(min, andword="")+ " minutes").capitalize()
    return texto


if __name__ == "__main__":
    main()
