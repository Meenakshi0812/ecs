# app.py

import requests
import random

def save_random_image():
    url = "https://source.unsplash.com/random"
    response = requests.get(url)
    if response.status_code == 200:
        image_name = f"random_image_{random.randint(1, 100)}.jpg"
        with open(image_name, 'wb') as image_file:
            image_file.write(response.content)
        return image_name
    else:
        return None

if __name__ == '__main__':
    image_file = save_random_image()
    if image_file:
        print(f"Random image saved as: {image_file}")
    else:
        print("Failed to fetch random image.")
