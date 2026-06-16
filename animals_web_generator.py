import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
ANIMALS_FILE = BASE_DIR / "animals_data.json"
ANIMALS_HTML_FILE = BASE_DIR / "animals_template.html"
ANIMALS_TO_HTML_FILE = BASE_DIR / "animals.html"
def generate_animals_from_json(ANIMALS_FILE):
    with open(ANIMALS_FILE, "r") as file:
        animals = json.load(file)
    return animals

def generate_animals_from_html(ANIMALS_HTML_FILE):
    with open(ANIMALS_HTML_FILE, "r") as file:
        html_as_string = file.read()
    return html_as_string

def generate_animals_to_html(output):
    with open(ANIMALS_TO_HTML_FILE, "w") as file:
        file.write(output)
    return output

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
        location,
        prey,
        name_of_young,
        group_behavior,
        estimated_population_size,
        biggest_threat,
        most_distinctive_feature,
        other_name,
        gestation_period,
        litter_size,
        habitat,
        diet,
        type_,
        number_of_species,
        color,
        skin_type,
        top_speed,
        lifespan,
        weight,
        length,
        age_of_sexual_maturity,
        age_of_weaning,
        distinctive_feature,
        temperament,
        training,
        average_litter_size,
        common_name,
        slogan,
        group
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
        self.location = location   # Einzelort (Chile etc.)

        # Characteristics
        self.prey = prey
        self.name_of_young = name_of_young
        self.group_behavior = group_behavior
        self.estimated_population_size = estimated_population_size
        self.biggest_threat = biggest_threat
        self.most_distinctive_feature = most_distinctive_feature
        self.other_name = other_name
        self.gestation_period = gestation_period
        self.litter_size = litter_size
        self.habitat = habitat
        self.diet = diet
        self.type = type_
        self.number_of_species = number_of_species
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
        self.average_litter_size = average_litter_size
        self.common_name = common_name
        self.slogan = slogan
        self.group = group

        # ⭐ Automatische Liste aller Attribute
        self.attributes = list(self.__dict__.keys())


@staticmethod
def from_dict(data: dict):
    taxonomy = data["taxonomy"]
    characteristics = data["characteristics"]

    # --- Location vereinheitlichen ---
    location_list = data.get("locations", [])

    # Sonderfall: "location" in characteristics
    single_location = characteristics.get("location")
    if single_location:
        if isinstance(location_list, list):
            location_list.append(single_location)
        else:
            location_list = [location_list, single_location]

    return Animal(
        name=data.get("name"),
        kingdom=taxonomy.get("kingdom"),
        phylum=taxonomy.get("phylum"),
        animal_class=taxonomy.get("class"),
        order=taxonomy.get("order"),
        family=taxonomy.get("family"),
        genus=taxonomy.get("genus"),
        scientific_name=taxonomy.get("scientific_name"),
        locations=location_list,
        location=single_location,

        # Characteristics (alte Felder)
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
        lifespan=characteristics.get("lifespan"),

        # Neue Felder
        prey=characteristics.get("prey") or characteristics.get("main_prey"),
        name_of_young=characteristics.get("name_of_young"),
        group_behavior=characteristics.get("group_behavior"),
        estimated_population_size=characteristics.get("estimated_population_size"),
        biggest_threat=characteristics.get("biggest_threat"),
        most_distinctive_feature=characteristics.get("most_distinctive_feature"),
        other_name=characteristics.get("other_name(s)"),
        gestation_period=characteristics.get("gestation_period"),
        litter_size=characteristics.get("litter_size"),
        habitat=characteristics.get("habitat"),
        number_of_species=characteristics.get("number_of_species"),
        top_speed=characteristics.get("top_speed"),
        weight=characteristics.get("weight"),
        length=characteristics.get("length"),
        age_of_sexual_maturity=characteristics.get("age_of_sexual_maturity"),
        age_of_weaning=characteristics.get("age_of_weaning")
    )



class AnimalRepository:
    def __init__(self, animals_list: dict = None) -> None:
        self.animals = []

        if animals_list:
            for animal_dict in animals_list:
                animals = from_dict(animal_dict)
                self.animals.append(animals)

def main():
    output = ""
    output_dict = {}
    search_for_str = "__REPLACE_ANIMALS_INFO__"
    if ANIMALS_FILE.exists():
        animals_data = generate_animals_from_json(ANIMALS_FILE)
    else:
        print("JSON-File not found")
        return
    if ANIMALS_HTML_FILE.exists():
        animals_html = generate_animals_from_html(ANIMALS_HTML_FILE)
       # soup = BeautifulSoup(animals_html)
    else:
        print("HTML-File not found")

    if animals_data:
        animal_repository = AnimalRepository(animals_data)
        for animal in animal_repository.animals:
            if animal.location:
                value_location = animal.location
            else:
                value_location = ""

            if animal.type:
                value_type = animal.type
            else:
                value_type = ""
            ''' for debugging:'''
            output += (f" Name: {animal.name}\n"
                       f" Diet: {animal.diet}\n"
                       f" Location: {value_location}\n"
                       f" Type: {value_type}")
            #print(output)
            # build html output
            output_dict[animal.name] = {
                "diet": animal.diet,
                "location": value_location,
                "type": value_type
            }
    else:
        print("No animals found")
        
    if search_for_str in animals_html:
        html_as_string = animals_html.replace(search_for_str, str(output))

    generate_animals_to_html(html_as_string)


    return

if __name__ == "__main__":
    main()