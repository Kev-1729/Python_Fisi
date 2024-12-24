def main():
    texto = input("Ingrese texto: ")
    print(convert(texto))

def convert(texto):
    texto = texto.replace(":)","🙂")
    texto = texto.replace(":(","🙁")
    return texto

main()
