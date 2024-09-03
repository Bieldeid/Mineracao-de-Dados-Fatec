import pandas as pd
import json

credits = pd.read_csv("tmdb_5000_credits.csv", header=0)

print(credits.head())

cast = credits['cast'].apply(json.loads).to_list()
title = credits['title'].to_list()

for x in range (len(title)):
    movie = cast[x]
    i=0
    aux = "Filme: " + title[x] + "\nAtores: "
    for actor in cast[x]:
        i += 1
        if(i < 3):
            aux += " " + actor['name'] + " | "
        else:
            break
    print(aux.rstrip(" | "))