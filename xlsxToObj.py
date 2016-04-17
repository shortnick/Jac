# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 12:04:45 2016

@author: shortnick
"""
from openpyxl import load_workbook
from geojson import Feature, Point, FeatureCollection #https://github.com/frewsxcv/python-geojson
from decimal import Decimal

class checkinObj(object):
    """holds Name, Description, Time, Coords of jac's 4square checkins"""
    def __init__(self, name, desc, time, coords):
        self.name = name
        self.desc = desc
        self.time = time
        self.coords = coords


biglist =[]
jsonlist=[]
Locations=[]
wb = load_workbook(filename = 'JacsPlaces.xlsx')
sheet_ranges = wb['checkinstrip']

for row in range(2,255):
    #to learn: why is 'int not iterable'?--for cell in row:
    cells = ['A','B','C','D']
    checkin = []    
    for letter in cells:  
        checkin.append((sheet_ranges[letter+str(row)].value))
#gotta be a better format http://www.diveintopython.net/native_data_types/formatting_strings.html
    biglist.append(checkinObj(checkin[0],checkin[1],checkin[2],checkin[3]))
for a in biglist:
    #print (dir(a)[-4:]) - gives script defined attr of checkinObj
    y,x = a.coords.split(" ")    
    loc = Point((Decimal(x),Decimal(y)))
    '''TypeError: Decimal('-122.31682872573953') is not JSON serializable'''
    "User written classes (checkinObj) don't have auto-coercion methods"
    Locations.append(Feature(geometry=loc, properties={"Name": a.name, "Description": a.desc, "When":a.time}))

print(Locations)
# parse location element. feed it into a geojson Point function
# feed these details into a Feature function, add to new list
#--example: Feature(geometry=my_point, properties={"country": "Spain"})
# dump that list into a Feature Collection funciton

#for feature collection: create a feature collection. 
    #it has a 'features' array inside, which is where all the feature objects go
        
#print(jsonlist)
print ("done")