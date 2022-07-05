import requests

url = 'https://www.advantour.com/img/kyrgyzstan/issyk-kul/issyk-kul.jpg'

res = requests.get(url)
print(res.content)

name = "photos/photo1.jpg"

with open(name, "wb") as file:
    file.write(res.content)