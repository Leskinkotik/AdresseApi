import requests

url = "https://api-adresse.data.gouv.fr/search/?q=stalingrad&postcode=92190"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # Looking for the name of the city
    if 'features' in data and len(data['features']) > 0:
        first_result = data['features'][0]
        if 'properties' in first_result:
            properties = first_result['properties']
            print("City", properties['city'])
    else:
        print("not found")
else:
    print("error:", response.status_code)
