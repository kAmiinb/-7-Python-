import requests

def get_random_dog_image_by_breed(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['message']
    else:
        return "Помилка при отриманні зображення собаки."
    
breed = "hound"
random_dog_image = get_random_dog_image_by_breed(breed)
print(f"Отримано випадкове зображення собаки породи {breed}: {random_dog_image}")
