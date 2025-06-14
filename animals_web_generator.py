import json

def load_data(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data

animals_data = load_data("animals_data.json")
output = ''
for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]
    try:
        type = animal["characteristics"]["type"]
    except KeyError:
        type = None
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{name}</div>\n'
    output += f'<p class="card__text">\n'
    output += f'<strong>Diet:</strong> {diet}<br/>\n'
    output += f'<strong>Location:</strong> {location}<br/>\n'
    if type is not None:
        output += f'<strong>Type:</strong> {type}<br/>\n'
    else:
        output += f""
    output += '</p></li>\n'
print(output)

with open("animals_template.html", "r") as template:
    template = template.read()

template = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as animals_data:
    animals_data.write(template)