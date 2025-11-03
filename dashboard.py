import matplotlib.pyplot as plt
import seaborn as sns

def exibir_dashboard(df): #vai receber o dataframe
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.catplot(
    x = "Estado", y = "Casos confirmados: ", data = df.sort_values("Casos confirmados", ascending = False), palette = "viridis")

    plt.title("Casos confirmados de COVID-19 por estado(última atualização feita:)")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()




























