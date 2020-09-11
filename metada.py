import pandas as pd
import numpy as np

fichier = "ratings.csv"
fichiers = ["credits.csv", "keywords.csv", "links.csv","links_small.csv","movies_metadata.csv","ratings.csv","ratings_small.csv"]


for fichier in fichiers:
    link = "data_csv/"+fichier
    data = pd.read_csv(link)
    print(fichier)
for i in range(len(data.columns)):
    print(data.iloc[0:10,i])