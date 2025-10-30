import requests
import pandas as pd


def obter_dados_covid():
    BASE = "https://brasil.io/api/dataset/covid19/caso/data/" #endpoint base do brasil.io para casos (documentação na página do dataset)

#parâmetros de filtros
    params = {
        "place_type": "state",
        "is_last": "false",
        "format": "json",
}
    resp = requests.get(BASE, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data["results"]) #transformar registros em dataframe
    print("Registros baixados:", len(df))

#salvamento local
    df.to_csv("casos_state_brasilio.csv", index = False)


