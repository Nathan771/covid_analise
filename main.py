from download_data import obter_dados_covid
from processamento import trat_dados
from dashboard import exibir_dashboard

def main():
    df = obter_dados_covid()
    df_tratado = trat_dados(df)
    exibir_dashboard(df_tratado)


if __name__ == "__main__":
    main()