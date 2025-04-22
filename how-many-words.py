import requests

url = 'https://dummyjson.com/carts'
response = requests.get(url)
data = response.json()

print(data)


       

        
