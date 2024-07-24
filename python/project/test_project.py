from project import informacion, actualizar, grafico_lineplot
import pytest
import requests
import os
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd


def main():
    test_informacion()
    test_actualizar()


def test_informacion():
    assert isinstance(
        informacion("https://www.senamhi.gob.pe/?p=pronostico-meteorologico"), str
    )
    with pytest.raises(requests.exceptions.RequestException):
        informacion("www.paginaFalsa.com")


def test_actualizar():
    datos_prueba = [
        [{"lugar": "Lugar1", "dia": "01 de enero", "t_mayor": 25.0, "t_menor": 15.0}],
        [{"lugar": "Lugar2", "dia": "02 de enero", "t_mayor": 30.0, "t_menor": 20.0}],
    ]
    archivo = "archivo_prueba.csv"

    actualizar(datos_prueba, archivo)
    assert os.path.isfile(archivo)


@pytest.fixture
def datos_vacios():
    datos = {
        "dia": ["01", "02", "03"],
        "t_mayor": [25, 28, 30],
        "t_menor": [15, 18, 20],
    }
    return pd.DataFrame(datos)


def test_grafico(datos_vacios):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    grafico_lineplot(datos_vacios, "UbicacionEjemplo")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    assert buf.read(8) == b"\x89PNG\r\n\x1a\n"

    plt.close()


if __name__ == "__main__":
    main()
