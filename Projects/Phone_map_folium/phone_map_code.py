# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:25:40 2023

@author: Brenda Rojas Delgado
"""

import webbrowser

# Making a map using the folium module
import folium
phone_map = folium.Map()

# Top three smart phone companies by market share in 2016
companies = [
    {'loc': [37.4970,  127.0266], 'label': 'Samsung: 20.5%'},
    {'loc': [37.3318, -122.0311], 'label': 'Apple: 14.4%'},
    {'loc': [22.5431,  114.0579], 'label': 'Huawei: 8.9%'}] 

# Adding markers to the map
for company in companies:
    marker = folium.Marker(location=company['loc'], popup=company['label'])
    marker.add_to(phone_map)

# The last object in the cell always gets shown in the notebook
phone_map.save("phone_map.html")
#webbrowser.open('C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Projects/Phone_map_folium\phone_map.html')
#or
webbrowser.open(r"C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Projects\Phone_map_folium\phone_map.html")