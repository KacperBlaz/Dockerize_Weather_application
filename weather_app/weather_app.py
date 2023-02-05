#from urllib.request import urlopen
#import urllib.parse
import requests
import json
import csv
import math



#TAKING DATA FROM API FOR SELECTED CITY
def get_api_data():
    api_endopint= "http://api.openweathermap.org/data/2.5/weather"
    city = "Barlinek"
    apikey = "eafba5712575b94d26865994d05cb3e3"
    url = api_endopint + "?q=" + city + "&appid=" + apikey
    request_url = requests.get(url)
    if request_url.status_code == 200:
        data = json.loads(request_url.text)
        return data

print(get_api_data())

# CELCIUS = Calvins - 273.15
#CONVERTING CALVINS TO CELCIUS
def args_from_output(api_response):
        added_data_to_csv = []
        city = api_response['name']
        temperature = api_response['main']['temp']
        convert_temperature = str(round(temperature - 273.15, 1)) + "℃"
        added_data_to_csv.append(city)
        added_data_to_csv.append(convert_temperature)
        return added_data_to_csv


print(args_from_output(get_api_data()))

#ADDING DATA FROM FUNCTION args_from_output TO CSV FILE
def add_data_to_csv_file(csv_file, args):
    with open(csv_file,'w', newline="") as file:
        header = ['Name','Temperature']
        imported_data = args[0], args[1]
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerow(imported_data)


print(add_data_to_csv_file('data.csv', args_from_output(get_api_data())))