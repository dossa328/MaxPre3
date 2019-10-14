from parse import parse
import json

with open('edges.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

SeoulMetro_list = []
for i in json_data:
    # SeoulMetro_list[i] = []
    SeoulMetro_list.append(i)
    for j in json_data[i]:
        SeoulMetro_list.extend([j["to"]])
        # SeoulMetro_list[i] = j["from"], j["to"]


# result = parse('"from":"{}","to":"{}","distance":3000,"time":5', '"from":"서동탄","to":"병점","distance":3000,"time":5')
# result = parse("The {} who say {}", "The knights who say Ni!")

# print(result)
# print(result.fixed)
print(SeoulMetro_list)
