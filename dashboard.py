import matplotlib.pyplot as plt
import seaborn as sns

def exibir_dashboard(df): #vai receber o dataframe
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.catplot(
    x = "Estado", y = "Casos confirmados: ", data = df.sort_values("Casos confirmados", ascending = False), palette = "viridis"
    )