import pandas as pd


def cargaDF(año):
    path = f"../ficheros_curso/names/yob{año}.txt"
    df = pd.read_csv(path, header=None, names=["nombre", "sexo", "cuenta"])
    df.set_index(["nombre","sexo"], inplace=True)
    return df

def sumarAños(año1, año2):
    df1 = cargaDF(año1)
    df2 = cargaDF(año2)
    #suma = df1 + df2
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("cuenta", ascending=False, inplace=True)
    return suma


if __name__ == "__main__":
    # df = cargaDF(2000)
    # print(df.head())

    suma = sumarAños(2000, 2001)
    print(suma.head())
