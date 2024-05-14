import pandas as pd
import os

# Lista de anos
anos = list(range(2021, 2022))
grand_prix_list = []
archives = []


# Itera sobre cada ano na lista 'anos'
for ano in anos:
    # Caminho do arquivo de entrada
    caminho_arquivo_entrada = (
        f"./data/qualifying_race_results/{ano}/Race Results/overall_race_results.csv"
    )

    # Lê o arquivo CSV para o DataFrame
    df = pd.read_csv(caminho_arquivo_entrada)

    # Renomear a coluna "Grand Prix"
    grand_prix_list.append(df["Grand Prix"].tolist())

for ano in anos:
    directory = f"./data/qualifying_race_results/{ano}/Qualifying Results/"
    archive = os.listdir(directory)
    archives.append(archive)

count = 1

print(grand_prix_list)


for archive, grand, ano in zip(archives, grand_prix_list, anos):
    directory = f"./data/qualifying_race_results/{ano}/Qualifying Results/"
    for gra in grand:
        name = str(count) + "_" + gra + "_"
        for arch in archive:
            partes = arch.split("_")
            if partes[0] == gra:
                new_name = name + partes[1] + "_" + partes[2]
                os.rename(
                    f"./data/qualifying_race_results/{ano}/Qualifying Results/{arch}",
                    f"./data/qualifying_race_results/{ano}/Qualifying Results/{new_name}",
                )
            else:
                continue
        count += 1
    count = 1
