import json

BASE_DIR = Path(__file__).resolve().parent
MOVIE_FILE = BASE_DIR / "animals.json"


def generate_animals_web():
    with open(MOVIE_FILE, "r") as file:
        animals = json.load(file)
    return animals
animals = generate_animals_web()
print(animals)
print(type(animals))
