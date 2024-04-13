"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.dropna()

    for column in df.columns:
        try:
            # df[column] = df[column].str.strip()
            df[column] = df[column].str.lower()
        except:
            pass
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="mixed", dayfirst=True
    )
    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)

    df["barrio"] = df["barrio"].str.replace(r"[\-\_]", " ", regex=True)
    # df["barrio"] = df["barrio"].str.strip()
    # df["barrio"] = df["barrio"].str.replace("nari¿o", "nariño")
    # df["barrio"] = df["barrio"].str.replace("bel?n", "belen")

    df["idea_negocio"] = df["idea_negocio"].str.replace(r"[\s+\-\_]", " ", regex=True)
    df["idea_negocio"] = df["idea_negocio"].str.strip()
    df["línea_credito"] = df["línea_credito"].str.replace(r"[\s+\-\_]", "", regex=True)
    # df["línea_credito"] = df["línea_credito"].str.replace("solidiaria", "solidaria")
    df = df.drop_duplicates()

    return df


clean_data()
