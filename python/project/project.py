import requests
from bs4 import BeautifulSoup
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd
import sys
from datetime import datetime, time


def main():
    website = sys.argv[1]
    contenedor = informacion(website)
    lugar_de_busqueda = input("Lugar: ")
    soup = BeautifulSoup(contenedor, "lxml")
    box = soup.find("tbody", class_="buscar")
    filas = box.find_all("tr")
    d = []

    for lugar in filas:
        parte = lugar.find_all("div", class_="row m-3")
        locacion = lugar.find("span", class_="nameCity").get_text()
        c = []
        for p in parte:
            try:
                dia = p.find("div", class_="col-sm-3").get_text()
                t_mayor = p.find("div", class_="col-sm-1 text-danger").get_text()
                t_menor = p.find("div", class_="col-sm-1 text-primary").get_text()
                descripcion = p.find("div", class_="col-sm-6").get_text()
                l = {
                    "lugar": locacion,
                    "dia": dia,
                    "t_mayor": t_mayor,
                    "t_menor": t_menor,
                    "descripcion": descripcion,
                }
                c.append(l)
            except:
                pass
        d.append(c)
    archivo = "Clima_Historial.csv"
    actualizar(d, archivo)

    df = pd.read_csv("Clima_Historial.csv")

    df["t_mayor"] = df["t_mayor"].replace("ºC", "", regex=True).astype(float)
    df["t_menor"] = df["t_menor"].replace("ºC", "", regex=True).astype(float)
    df["dia"] = df["dia"].apply(lambda x: x.split(", ")[1].strip())
    df[["zona", "departamento"]] = df["lugar"].str.split(" - ", expand=True)
    try:
        zona, departamento = lugar_de_busqueda.split(" - ")
        df = df.drop(columns=["lugar"])
        datos_del_lugar = df[df["zona"] == zona]
        datos_del_departamento = df[df["departamento"] == departamento]
    except:
        print("No se encontro ese Lugar.")

    grafico_lineplot(datos_del_lugar, zona)
    grafico_lineplot(datos_del_departamento, departamento)
    grafico_puntos(datos_del_lugar, zona)
    grafico_puntos(datos_del_departamento, departamento)


def informacion(website):
    try:
        resultado = requests.get(website)
        resultado.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
        raise
    else:
        return resultado.text


def actualizar(d, archivo):
    if (
        not os.path.isfile(archivo)
        or os.path.getsize(archivo) == 0
        or datetime.now().time() < time(20, 0)
    ):
        with open(archivo, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=d[0][0].keys())
            writer.writeheader()

        verificar = set()
        with open(archivo, "r") as file:
            reader = csv.DictReader(file)
            verificar = {(row["lugar"], row["dia"]) for row in reader}

        with open(archivo, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=d[0][0].keys())
            for sublist in d:
                for row in sublist:
                    if (row["lugar"], row["dia"]) not in verificar:
                        writer.writerow(row)
                        verificar.add((row["lugar"], row["dia"]))


def grafico_lineplot(df, ubicacion):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.lineplot(x="dia", y="t_mayor", data=df, label="Temp. Mayor", marker="o")
    sns.lineplot(x="dia", y="t_menor", data=df, label="Temp. Menor", marker="o")

    plt.title(f"Temperatura a lo largo de los dias {ubicacion}")
    plt.xlabel("Dia")
    plt.ylabel("Temperatura °C")
    plt.legend()
    plt.ylim(0, 50)
    plt.savefig(f"grafica_temperatura_{ubicacion}.png")


def grafico_puntos(df, ubicacion):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["dia"], df["t_mayor"], color="skyblue", label="Temp. Mayor", marker="o"
    )

    plt.scatter(
        df["dia"], df["t_menor"], color="lightcoral", label="Temp. Menor", marker="o"
    )

    plt.title(f"Dispersión de Temperaturas a lo largo de los días en {ubicacion}")
    plt.xlabel("Día")
    plt.ylabel("Temperatura °C")
    plt.legend()
    plt.ylim(0, 50)
    plt.savefig(f"puntos_temperatura_{ubicacion}.png")


if __name__ == "__main__":
    main()
