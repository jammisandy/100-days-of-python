import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "a4d1dd6ad212c5c0f14fd3f82b242d1f"
account_sid = "AC636f6c2d70b7af89d802073efa1dc383"
auth_token = "a5e16c13cdbb25a604080ef8d1a96ead"


weather_params = {
    "lat": 27.200001,
    "lon": 77.037003,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(result["list"][0]["weather"][0]["id"])
# print(response.json())

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 1000:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token) 
    message = client.messages \
                    .create(
                         body="It's going to rain today, Please Bring an umbrella",
                         from_='+12566188877',
                         to='+919035932042'
                     )

    print(message.Status)