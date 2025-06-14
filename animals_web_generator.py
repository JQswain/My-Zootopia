import json

def load_data(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data

animals_data = load_data("animals_data.json")

for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]
    try:
        type = animal["characteristics"]["type"]
    except KeyError:
        type = None
    print(f"Name: {name} \nDiet: {diet} \nLocation: {location}")
    if type is not None:
        print(f"Type: {type}\n")
    else:
        print()