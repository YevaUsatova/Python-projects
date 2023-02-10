#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: November 2020
# This program shows the location on the map from CSV file

import folium
import pandas as pd

cname=input("Enter CSV file name: ")
outname= input("Enter output file: ")

cn=pd.read_csv(cname)
mapNYC=folium.Map(location=[40.75,-74.125])

for index,row in cn.iterrows():
    lat=row["LATITUDE"]
    lon=row["LONGITUDE"]
    name=row["TIME"]
    folium.Marker(location=[lat, lon],popup= name).add_to(mapNYC)
mapNYC.save(outname)
