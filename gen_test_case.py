import json
import random
import threading
from threading import Thread

import alpha_pruning
import dijkstra
import numpy as np
from Graph import Graph
# ws_choi
import findallpaths2
# hd_jung
import signal
import time

from Metro import Metro

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)

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
time_out = 3

metro = Metro()

for i in range(10000):
    ran_start, ran_end = rand_start_end(data_set)

    done_counting = threading.Event()
    t = threading.Thread(target=alpha_pruning.get_result, args=(metro, ran_start, ran_end, alpha))
    t.setDaemon(True)

    t.start()

    t.join(time_out)
    done_counting.wait(time_out)
    if t.is_alive():
        print(ran_start, ran_end)
        pass

    else:
        pass
