import requests

params = {
    "q": "stalingrad",
    "limit": 15  # Указываем лимит для получения первых 15 результатов
}

url = "https://api-adresse.data.gouv.fr/search/?q=stalingrad&limit=15"

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    # Проверяем, что есть результаты
    if 'features' in data and len(data['features']) > 0:
        for result in data['features']:
            if 'properties' in result:
                properties = result['properties']
                if 'city' in properties:
                    print("City:", properties['city'])
                else:
                    print("City not found for this result.")
    else:
        print("No results found.")
else:
    print("Error:", response.status_code)
