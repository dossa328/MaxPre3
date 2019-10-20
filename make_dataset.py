import json
from collections import OrderedDict

file_data = OrderedDict()
# 887
# 876
for i in range(1):
    input_vertex = input().split(',')
    file_data[i] = {"from":input_vertex[0], "to":input_vertex[1]}

with open('input_data2.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
