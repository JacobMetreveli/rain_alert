import requests
from twilio.rest import Client

account_sid = 'AC31a7b691abe8e41b11c724e75d27f678'
auth_token = 'd1e1bb1999f407e5c0f21f30be634f8f'

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "8602fea70f35af896274a1f6a6daddad"

weather_params = {
    'lat': 31.9730,
    'lon': 34.7925,
    'appid': API_KEY
}

response = requests.get(OWM_endpoint, params=weather_params)

weather_data = response.json()

daily_prognose = weather_data['list'][:5]

will_rain = False

for section in daily_prognose:
    if section['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+15855172707',
        to='+972534751152'
    )
    print(message.status)
