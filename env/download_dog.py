import requests

dog_json = requests.get("https://dog.ceo/api/breeds/image/random").json()

impg_url = dog_json["message"]

image_response = requests.get(impg_url)

with open("dog.jpg", "wb") as file:
    for chunk in image_response.iter_content():
        file.write(chunk)
