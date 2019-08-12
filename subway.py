import json

with open('edges2.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

    print(json_data)
