#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: November 2020
# This program shows the location on the map from CSV file

import folium
import pandas as pd

name=input("Please enter the name of the input file: ")
outname= input("Please enter the name of the output file: ")
br= input ("Please enter the name of the borough: ")

cn=pd.read_csv(name)
mapNYC=folium.Map(location=[40.75,-74.125])
cnCopy = cn.groupby("Borough").get_group(br)

for index,row in cnCopy.iterrows():
    lat=row["Latitude"]
    lon=row["Longitude"]
    name=row["Address"]
    folium.Marker(location=[lat, lon],popup= name).add_to(mapNYC)
mapNYC.save(outname)
