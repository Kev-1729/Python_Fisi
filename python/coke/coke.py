'''
Supongamos que una máquina vende botellas de Coca-Cola (Coca-Cola) a 50 céntimos y sólo acepta monedas de estas denominaciones: 25 céntimos, 10 céntimos y 5 céntimos.
'''
def main():
    costo = 50
    p = 0
    while 0 <= costo:

        print(f"1Amount Due: {costo}")
        p = int(input("Insert Coin: "))

        if p == 5 or p == 10 or p == 25:
            costo -= p

        else:
            print(f"2Amount Due: {costo}")

        if costo <= 0:
            print(f"Change Owed: {-1*costo}")
            break

main()
