# API Ninjas key:
API_KEY = "NGvVjduynuMZhmbQ07E7yQhMLvLZFRXtOB3E3uEp"

import requests

BASE_URL = "https://api.api-ninjas.com/v1/"


def fetch_animal_details(animal):
    request_URL = f"{BASE_URL}animals?name={animal}"
    headers = {"X-Api-Key": API_KEY}
    print("Making the following request", request_URL)
    animals = requests.get(request_URL, headers)
    print("Result of the request", animals)
    animals = animals.json()
    for animal in animals:
        print(animal)


def main():
    fetch_animal_details("foxyfoxtrot")


if __name__ == "__main__":
    main()
