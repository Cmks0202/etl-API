import requests 

url = 'https://www.globo.com/'

resposta = requests.get(url)

print(resposta)
