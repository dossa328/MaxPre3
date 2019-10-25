import json
from collections import OrderedDict

file_data = OrderedDict()
# file_data = []
# 887
# 876
# 기초 데이터
# for i in range(2625):
#     ff_data = []
#     input_vertex = input().split(',')
#     # file_data[i] = {"from":input_vertex[0], "to":input_vertex[1]}
#     # ff_data = [input_vertex[0], input_vertex[1]]
#     # if not ff_data in file_data:
#     #     print(input_vertex[0],",",input_vertex[1])
#     file_data[i] = {"from": input_vertex[0], "to": input_vertex[1]}
#     # file_data.append([input_vertex[0], input_vertex[1]])
#
#
# with open('trans_classification_list.json', 'w', encoding="utf-8") as make_file:
#     json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

for i in range(700):
    input_vertex = input().split(',')
    file_data[i] = {"num_of":input_vertex[0], "from":input_vertex[1], "to":input_vertex[2]}

with open('trans_classification_experiment_data.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
