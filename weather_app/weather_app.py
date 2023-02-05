#from urllib.request import urlopen
#import urllib.parse
import sys, os, requests, json, csv, math


API_KEY = os.environ.get('API_KEY')
CITY = 'Barlinek'
#TAKING DATA FROM API FOR SELECTED CITY
def get_api_data():
    api_endopint= "http://api.openweathermap.org/data/2.5/weather?q="+CITY+"&appid="+API_KEY
    request_url = requests.get(api_endopint)
    if request_url.status_code == 200:
        data = json.loads(request_url.text)
        return data

print(get_api_data())

# CELCIUS = Calvins - 273.15
#CONVERTING CALVINS TO CELCIUS
def args_from_output(api_response: dict) -> list:
        city = api_response['name']
        temperature = api_response['main']['temp']
        return [city, convert_temperature(temperature)]

def convert_temperature(temperature: str) -> str:
    return str(round(temperature - 273.15, 1)) + "℃"


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