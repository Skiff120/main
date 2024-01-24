import requests

response = requests.get("https://coinmarketcap.com/")
print(response.text)