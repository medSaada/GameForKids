import requests

url="http://172.20.10.2/data"
response = requests.get(url)

if response.status_code == 200:



    text = response.text
    print(text)
else:
    print(f"Erreur {response.status_code} lors de la récupération du fichier")