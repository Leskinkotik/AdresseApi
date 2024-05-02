import requests

url = "https://api-adresse.data.gouv.fr/reverse/?lon=2.234489&lat=48.814737"

response = requests.get(url)

# I need status 200
if response.status_code == 200:
    info = response.json()
    print(info['type'])
else:
    print("error:", response.status_code)

