import requests as req

res = req.get('https://jsonplaceholder.typicode.com/photos')
data = res.json()

with open('photo_urls.txt', 'w') as f:
    for photo in data:
        f.write(f"{photo['url']}\n")


