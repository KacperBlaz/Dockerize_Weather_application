import os
import requests
import json
import csv
import math
import mysql.connector


API_KEY = os.environ.get('API_KEY')
CITY = os.environ.get('CITY')
MYSQL_ROOT_LOGIN = os.environ.get('MYSQL_ROOT_LOGIN')
MYSQL_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')
DATABASE = os.environ.get('DATABASE')
FILE = 'data.csv'
TABLE_NAME = os.environ.get('TABLE_NAME')
DATABASE_IP = os.environ.get('DATABASE_IP')


#TAKING DATA FROM API FOR SELECTED CITY
def get_api_data(city, api_key: str) -> dict:
    api_endpoint= (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    request_url = requests.get(api_endpoint)
    if request_url.status_code == 200:
        data = json.loads(request_url.text)
        return data


#CONVERTING CALVINS TO CELCIUS
def args_from_output(api_response: dict) -> list:
    city = api_response['name']
    temperature = api_response['main']['temp']
    return [city, convert_temperature(temperature)]


def convert_temperature(temperature: str) -> str:
    return str(round(temperature - 273.15, 1)) + "℃"


#ADDING DATA FROM FUNCTION args_from_output TO CSV FILE
def add_data_to_csv_file(csv_file, args):
    with open(csv_file, 'w', newline="") as file:
        fieldnames = ['Name', 'Temperature']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"Name": args[0], "Temperature": args[1]})


#CREATING MYSQL DATABASE IN CONTAINER
def create_mysql_database(database_name: str) -> str:
        mydb = mysql.connector.connect(
        host = (f"{DATABASE_IP}"),
        user = (f"{MYSQL_ROOT_LOGIN}"),
        password = (f"{MYSQL_ROOT_PASSWORD}")
        )
        mycursor = mydb.cursor()
        try:
            mycursor.execute(f"CREATE DATABASE {database_name}")
            print(f"Database {database_name} has been created !")
        except mysql.connector.errors.DatabaseError:
            print(f"Error, database {database_name} exist! Skipping")


#CREATING A TABLE FROM CSV FILE
def import_csv_file_to_mysql_database(csv_file: str) -> str:
    add_table_to_database = (f"csvsql --db mysql+pymysql://{MYSQL_ROOT_LOGIN}:{MYSQL_ROOT_PASSWORD}@{DATABASE_IP}/{DATABASE} --tables "
    f"{TABLE_NAME} --insert {csv_file}")
    os.system(add_table_to_database)


#RUNNING FUNCTIONS
create_mysql_database(DATABASE)
print(args_from_output(get_api_data(CITY, API_KEY)))
add_data_to_csv_file(FILE, args_from_output(get_api_data(CITY, API_KEY)))
import_csv_file_to_mysql_database(FILE)