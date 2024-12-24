def main():

    list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        fecha = input("Date: ").title().strip()
        if "/" in fecha:
            mes, dia, anio = fecha.split("/")
            if mes.isdigit():
                if 1 <= int(dia) <=31:
                    if int(mes) > 12:
                        continue
                    if int(dia) < 10:
                        dia = "0"+dia
                    if int(mes) < 10:
                        mes = "0"+mes
                    print(f"{anio}-{mes}-{dia}")
                    break

        else:
            mes, dia, anio = fecha.split(" ")
            if "," in dia:
                dia = dia.replace(",","")
                if mes in list:
                    if 1 <= int(dia) <=31:
                        if int(dia) < 10:
                            dia = "0"+dia
                        if mes in list[0:10]:
                            mes = int(list.index(mes)+1)
                            if mes < 10:
                                mes = "0"+ str(mes)
                            print(f"{anio}-{mes}-{dia}")
                            break
            else:
                continue

main()
