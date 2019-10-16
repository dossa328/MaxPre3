import json
import random
import threading
import alpha_pruning
import straight_forward
import time
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


alpha_for_alpha_pruning = 1.1
alpha_for_straight_forward = 1.0
metro = Metro()
alpha_pruning_result = []
alpha_pruning_result_avg = 0
straight_forward_result = []
straight_forward_result_avg = 0
for j in range(len(input_data)):
    start_time = time.time()
    alpha_pruning_result.append(alpha_pruning.get_result(metro, input_data[str(j)]['from'], input_data[str(j)]['to'], alpha_for_alpha_pruning))
    alpha_pruning_result_avg = alpha_pruning_result_avg + alpha_pruning_result[j][2]

end_time = time.time()
print(alpha_pruning_result_avg / len(input_data))
print("AP_WorkingTime: {} sec".format(end_time-start_time))

for j in range(len(input_data)):
    start_time = time.time()
    straight_forward_result.append(straight_forward.get_result(metro, input_data[str(j)]['from'], input_data[str(j)]['to'], alpha_for_straight_forward))
    straight_forward_result_avg = straight_forward_result_avg + straight_forward_result[j][2]

end_time = time.time()
print(straight_forward_result_avg / len(input_data))
print("SF_WorkingTime: {} sec".format(end_time - start_time))

#
# time_out = 3
# for i in range(10000):
#     ran_start, ran_end = rand_start_end(data_set)
#
#     done_counting = threading.Event()
#     # t = threading.Thread(target=alpha_pruning.get_result, args=(metro, ran_start, ran_end, alpha))
#     t = threading.Thread(target=straight_forward.get_result, args=(metro, ran_start, ran_end, alpha))
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