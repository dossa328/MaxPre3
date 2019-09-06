import json
from collections import OrderedDict

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)


transline = []
file_data = OrderedDict()

for i in line_data:
    for j in line_data[i]:
        for k in line_data:
            for l in line_data[k]:
                if i == k and j == l:
                    pass
                elif j == l:
                    transline.append({"from": j + i, "to": l + k, "distance": 999, "time": 3})
                    #transline.append({"from": l + k, "to": j + i, "distance": 999, "time": 3})
                    # file_data = ["from":j, "to":l, "time":3]


print(transline)

'''
for i in range(10):
    file_data[i] = [{"from":"신당","to":"신당2"}]

with open('words.json','w',encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
'''
