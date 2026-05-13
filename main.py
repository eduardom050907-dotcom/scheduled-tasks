import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 43.009739
MY_LONG = -7.556758

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_phone = os.environ.get("MY_PHONE_NUMBER")

parameters={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key,
    "cnt":4,
}

response=requests.get(url=OWM_endpoint,params=parameters)
response.raise_for_status()
weather_data=response.json()

test=0
weather_ids=[weather_data["list"][ind]["weather"][0]["id"]for ind in range (4)]
for id in weather_ids:
    if id<700:
        test+=1

if test>0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella",
        from_="+15075981783",
        to=my_phone,
    )
    print(message.status)
