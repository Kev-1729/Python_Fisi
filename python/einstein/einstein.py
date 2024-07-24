def main():
    masa = int(input("Ingrese la masa: "))
    print(int(julios(masa)))

def julios(masa):
    c = 300000000
    E = masa * c**2
    return E

main()

