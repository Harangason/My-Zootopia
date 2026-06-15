import json

BASE_DIR = Path(__file__).resolve().parent
MOVIE_FILE = BASE_DIR / "animals.json"


def generate_animals_web():
    with open(MOVIE_FILE, "r") as file:
        animals = json.load(file)
    return animals

animals = generate_animals_from_json(ANIMALS_FILE)

class Animal:
    def __init__(
        self,
        name,
        kingdom,
        phylum,
        animal_class,
        order,
        family,
        genus,
        scientific_name,
        locations,
        distinctive_feature,
        temperament,
        training,
        diet,
        average_litter_size,
        type_,
        common_name,
        slogan,
        group,
        color,
        skin_type,
        lifespan
    ):
        self.name = name

        # Taxonomy
        self.kingdom = kingdom
        self.phylum = phylum
        self.animal_class = animal_class
        self.order = order
        self.family = family
        self.genus = genus
        self.scientific_name = scientific_name

        # Locations
        self.locations = locations

        # Characteristics
        self.distinctive_feature = distinctive_feature
        self.temperament = temperament
        self.training = training
        self.diet = diet
        self.average_litter_size = average_litter_size
        self.type = type_
        self.common_name = common_name
        self.slogan = slogan
        self.group = group
        self.color = color
        self.skin_type = skin_type
        self.lifespan = lifespan

    def __str__(self):
        return f"{self.name} ({self.scientific_name})"




'''



def main():

    if ANIMALS_FILE.exists():

    animals = generate_animals_web(ANIMALS_FILE)
    print(animals)
    print(type(animals))
