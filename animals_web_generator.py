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
        self.prey = pretty
        self.name_of_young = name_of_young
        self.group_behavior = group_behavior
        self.estimated_population_size = estimated_population_size
        self.biggest_threat = biggest_threat
        self.most_distinctive_feature =most_distinctive_feature
        self.other_name = other_name
        self.gestation_period =gestation_period
        self.litter_size = litter_size
        self.habitat = habitat
        self.diet = diet
        self.type = type_
        self.number_of_species =number_of_species
        self.location = locations
        self.color = color
        self.skin_type = skin_type
        self.top_speed = top_speed
        self.lifespan = lifespan
        self.weight = weight
        self.length = length
        self.age_of_sexual_maturity = age_of_sexual_maturity
        self.age_of_weaning = age_of_weaning
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

def animal_from_dict(data: dict) -> Animal:
    taxonomy = data["taxonomy"]
    characteristics = data["characteristics"]

        return Animal(
            name=data["name"],
            kingdom=taxonomy.get("kingdom"),
            phylum=taxonomy.get("phylum"),
            animal_class=taxonomy.get("class"),
            order=taxonomy.get("order"),
            family=taxonomy.get("family"),
            genus=taxonomy.get("genus"),
            scientific_name=taxonomy.get("scientific_name"),
            locations=data.get("locations", []),
            distinctive_feature=characteristics.get("distinctive_feature"),
            temperament=characteristics.get("temperament"),
            training=characteristics.get("training"),
            diet=characteristics.get("diet"),
            average_litter_size=characteristics.get("average_litter_size"),
            type_=characteristics.get("type"),
            common_name=characteristics.get("common_name"),
            slogan=characteristics.get("slogan"),
            group=characteristics.get("group"),
            color=characteristics.get("color"),
            skin_type=characteristics.get("skin_type"),
            lifespan=characteristics.get("lifespan")
        )

class AnimalRepository:
    def __init__(self, animals_list: dict = None) -> None:
        self.animals = []

        if animals_list:
            for animal_dict in animals_list:
                animals = Animal.from_dict(animal_dict)
                self.animals.append(animals)


repo = AnimalRepository(animals_data)
print(f"{repo.animals}")





def main():

    if ANIMALS_FILE.exists():
        animals_data = generate_animals_from_json(ANIMALS_FILE)
    else:
        print("File not found")
        return

    if animals_data:
        animal_repository = AnimalRepository(animals_data)
        for animal in animal_repository.animals:
            print(animal.name) # show name of animal
    else:
        print("No animals found")

   

    animals = generate_animals_web(ANIMALS_FILE)
    print(animals)
    print(type(animals))
