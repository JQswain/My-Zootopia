import json

def load_data(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data



def serialize_animals(animal_item):
    output = ''
    name = animal_item["name"]
    diet = animal_item["characteristics"]["diet"]
    location = animal_item["locations"][0]
    try:
        animal_type = animal_item["characteristics"]["type"]
    except KeyError:
        animal_type = None
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{name}</div>\n'
    output += f'<div class="card__text">\n'
    output += f'<ul>\n<li><strong>Diet:</strong> {diet}</li>\n'
    output += f'<li><strong>Location:</strong> {location}</li>\n'
    if animal_type is not None:
        output += f'<li><strong>Type:</strong> {animal_type}</li>\n'
    else:
        output += f""
    output += '</ul>\n</div>\n</li>\n'

    return output

def generate_html():
    animals_data = load_data("animals_data.json")
    output = ''
    for animal in animals_data:
        output += serialize_animals(animal)
        with open("animals_template.html", "r") as template:
            template = template.read()

    template = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as animals_data:
        animals_data.write(template)

def main():
   generate_html()

if __name__ == "__main__":
    main()