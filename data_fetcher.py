import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
URL_ANIMALS = f"https://api.api-ninjas.com/v1/animals"

def load_data(animal):
    """
    load animals data from api
    :param animal: animal to load
    :return: list of animals data
    """


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    headers  = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    try:
        response = requests.get(URL_ANIMALS, headers=headers, params=params)
        status_code = response.status_code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(e)


