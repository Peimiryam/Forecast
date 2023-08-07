#import datetime
from datetime import date

import requests, json

#API Endpoint URL: `https://api.open-meteo.com/v1/forecast?latitude=51.5085}&longitude=-0.1257&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={data}&end_date={data}`

#input a datetime

user_input = input("Hello, welcome to the forecast app. Input 'ok' if you want to check the today forecast or 'select' if you want to check a date: ")

if user_input == 'ok':

    time_data = date.today()

elif user_input == 'select':

    time_data = input("Input a date with this format 'YYYY-MM-DD' in order to check precipitation in London: ")

    print(f"Datetime selected: {time_data}")

API_URL = f'https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={time_data}&end_date={time_data}'

url = API_URL

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print(data)

    precipitation = data['daily']['precipitation_sum'][0]

    print(precipitation)

# "It will rain" for a result greater than 0.0.
    if precipitation > 0.0:
        print("it will rain :(")
#"It will not rain" for a result equal to 0.0
    elif precipitation == 0.0:
        print("it will not rain :)")
#"I don't know" when there is no result or the result is negative
    else:
        print("I don't know.")

else:
    # showing the error message
   print("Error in the HTTP request")

