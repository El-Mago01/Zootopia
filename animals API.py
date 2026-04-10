# API Ninjas key:
API_KEY = "NGvVjduynuMZhmbQ07E7yQhMLvLZFRXtOB3E3uEp"

import requests
import os

BASE_URL = "https://api.api-ninjas.com/v1/"


def get_animals_data(animal):
    request_URL = f"{BASE_URL}animals?name={animal}"
    headers = {"X-Api-Key": API_KEY}
    print("Making the following request", request_URL)
    animals = requests.get(request_URL, headers)
    print("Result of the request: ", end="")
    if "200" in animals.text:
        print("GET request successful!")
    animals = animals.json()
    return animals

def load_animals_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def load_html_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read()

def write_to_new_html_file(content):
    with open("animals.html", "w") as f:
        f.write(content)
        dir_path=os.path.dirname(os.path.realpath(__file__))
        print(f'File stored in: {dir_path}\\{f.name}')


def serialize_animal(animal):
    animal_repository_str=''
    animal_repository_str += f'<li class="cards__item">\n'
    animal_repository_str += f'<div class="card__title">\n'
    if "name" in animal:
        animal_repository_str += f'{animal['name']}</div>\n'
        animal_repository_str += f'<div class="card__text">\n'
        animal_repository_str += f'<ul>\n'
        if "taxonomy" in animal:
            if "scientific_name" in animal["taxonomy"]:
                animal_repository_str += f"<li><strong>Scientific name:</strong> {animal["taxonomy"]["scientific_name"]}</li>\n"
            if "characteristics" in animal:
                if "diet" in animal["characteristics"]:
                    animal_repository_str += f"<li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>\n"
            if "locations" in animal:
                animal_repository_str += f"<li><strong>Location:</strong> {animal["locations"][0]}</li>\n"
            if "characteristics" in animal:
                if "type" in animal["characteristics"]:
                    animal_repository_str += f"<li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>\n"
        #animal_repository_str+='</p>\n'
        animal_repository_str+='</ul>\n'
    else:
        animal_repository_str="ERROR: animal without a name"
    return animal_repository_str

def main():
    user_input=input("Animal: ")
    animals_data=get_animals_data(user_input)
    html_data = load_html_file("animals_template.html")
    __replace__ = "__REPLACE_ANIMALS_INFO__"

    animal_repository_string = ""

    # for each type of animal in the input json file, create a repository string
    for animal in animals_data:
        animal_repository_string += serialize_animal(animal)

    # The replacement below is necessary to avoid a mojibake
    animal_repository_string = animal_repository_string.replace("â€™", "\'")
    # Replace the string to replace in the html with the animal repository
    html_data = html_data.replace(__replace__, animal_repository_string)

    write_to_new_html_file(html_data)


if __name__ == "__main__":
    main()
