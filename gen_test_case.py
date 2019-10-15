import json
import random
import threading
import alpha_pruning
import cal_dijkstra_cost
from Metro import Metro

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)

with open('input_data.json', 'r', encoding='UTF-8') as data_file:
    input_data = json.load(data_file)

data_set = []

for i in line_data:
    for j in line_data[i]:
        data_set.append(j + i)


def rand_start_end(_data_set):
    while True:
        _start = random.choice(_data_set)
        _end = random.choice(_data_set)

        if _start is not _end:
            break

    return _start, _end


alpha = 1.1
metro = Metro()

for j in range(888):
    alpha_pruning.get_result(metro, input_data[str(j)]['from'], input_data[str(j)]['to'], alpha)
    cal_dijkstra_cost.dijkstra_get_cost(metro, input_data[str(j)]['from'], input_data[str(j)]['to'])

#
# time_out = 3
# for i in range(10000):
#     ran_start, ran_end = rand_start_end(data_set)
#
#     done_counting = threading.Event()
#     t = threading.Thread(target=alpha_pruning.get_result, args=(metro, ran_start, ran_end, alpha))
#     t.setDaemon(True)
#
#     t.start()
#
#     t.join(time_out)
#     done_counting.wait(time_out)
#     # if runtime out (difficult problem)
#     if t.is_alive():
#         # print(ran_start, ran_end)
#         pass
#     # if runtime out (easy problem)
#     else:
#         print(ran_start, ran_end)
#         # pass