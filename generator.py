import json
import random
import alpha_pruning
import dijkstra
import numpy as np
from Graph import Graph
# ws_choi
import findallpaths2
# hd_jung
import signal
import time

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)




dataset = []

for i in line_data:
    for j in line_data[i]:
        dataset.append(j+i)

run_times = 0
run_times2 = 0
alpha = 1.1
val = 1
ran_end = []
# for i in range(len(ran_end)):
dijkstra_result = np.load('Dijkstra_result.npy')
dijkstra_dict = {}
for r in dijkstra_result:
    dijkstra_dict[r[0]] = r[1]

ran_start = random.choice(dataset)
dijkstra.cal_dists(ran_start)
print(ran_start)

while 1:
    re_ran = random.choice(dataset)
    if int(dijkstra_dict[re_ran]) >= 60:
        pass
    else:
        if re_ran not in ran_end and not re_ran == ran_start:
            ran_end.append(re_ran)
        if len(ran_end) == val:
            break
print(ran_end)

for i in range(val):
    start = time.time()
    print(alpha_pruning.get_result(ran_start, ran_end[i], alpha))
    # print(findallpaths.ppp('신길5', '기흥E', alpha))
    run_times = run_times + time.time() - start
    print("ws", i, ran_end[i])

# for i in range(val):
#     start = time.time()
#     print(findallpaths2.ppp(ran_start, ran_end[i], alpha))
#     run_times2 = run_times2 + time.time() - start
#     print("jh", i, ran_end[i])

print("ws time :", run_times/val)
# print("jh time :", run_times2/val)

