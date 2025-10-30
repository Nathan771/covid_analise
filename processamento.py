def trat_dados(df):
    df["date"] = pd.to_datetime(df["date"])
    df = df.rename(columns={"confirmed": "Casos confirmados:", "deaths": "Óbitos" })
    return df