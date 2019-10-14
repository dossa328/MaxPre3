import json
from collections import OrderedDict

file_data = OrderedDict()

for i in range(888):
    input_vertex = input().split(',')
    file_data[i] = {"from":input_vertex[0], "to":input_vertex[1]}

with open('input_data.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
