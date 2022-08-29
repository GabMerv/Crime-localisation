import folium
import webbrowser
import pandas
from tqdm import tqdm

fichier = "test.html"
logo = "bomb"
couleur_Marker = "red"
couleur_icone = "white"

description_n = "Description"
location_n = "Location"
date_n = "Date"

latitudes = []
longitudes = []
descriptions = []
dates = []

file = pandas.read_csv("database.csv", usecols=[location_n, description_n, date_n])
maxPoints = 1000
i = 0

print("Traitement du fichier .csv...")
for el in tqdm(file[location_n]):
   if type(el) == str:
      el = el.split(",")
      el[0] = float(el[0][1:-1])
      el[1] = float(el[1][1:-1])
      latitudes.append(el[0])
      longitudes.append(el[1])
      descriptions.append(file[description_n][i])
      dates.append(file[date_n][i])
      i += 1
   if i==maxPoints:
      break
print("Création de la carte...")
carte = folium.Map(location = [latitudes[0], longitudes[0]], zoom_start=50, tiles="Stamen Toner")
print("Ajout des points...")
for i in tqdm(range(len(latitudes))):
   lon = longitudes[i]
   lat = latitudes[i]
   folium.Marker([lat, lon], icon=folium.Icon(icon=logo, color=couleur_Marker, icon_color=couleur_icone, prefix="fa"), popup=descriptions[i], tooltip=dates[i]).add_to(carte)

print("Sauvegarde de la carte...")
carte.save(fichier)
print("Ouverture de la carte...")
webbrowser.open(fichier)
