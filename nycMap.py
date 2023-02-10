#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: November 2020
# This program shows the location on the map

import folium
mapNYC=folium.Map(location=[40.75,-74.125],zoom_start=10)
folium.Marker(location=[40.768731, -73.964915],popup= "Hunter College").add_to(mapNYC)
mapNYC.save(outfile='nycMap.html')
