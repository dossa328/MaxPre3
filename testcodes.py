import json

with open('trans.json', 'r', encoding='UTF-8') as json_file:
    trans_data = json.load(json_file)

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)

line_data_keys = list(line_data.keys())
result = []
for i in trans_data["trans"]:
    kk = i
    for j in line_data_keys:
        if not kk == i:
            break
        else:
            kk = i.rstrip(j)
    result.append(kk)

result2 = list(set(result))
print(result2)
