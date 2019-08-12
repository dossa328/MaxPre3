# -*- coding: utf-8 -*-
# (up line) use utf-8 coding
from Graph import Graph
from copy import deepcopy as c
from Allpathweight import ap
import json
graph = Graph(undirected=True)
maximum_value = pow(2, 31)
input_way_edges = []
list_way_edges = {}
distance = {}
priority_Queue = []
distance2 = {}
in_start = '목동'
in_end = '오목교'
input_all_vertex = 0
# 밑에꺼 raw_input() 이었음..

# 전체 노선도 불러옴
# ------------------------------------------------------------------
with open('edges2.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

    # print(json_data)
# ------------------------------------------------------------------
# 불러온 노선도를 input 양식에 맞추기
# ------------------------------------------------------------------
SeoulMetro = {}
SeoulMetro_list = []
for i in json_data:
    SeoulMetro[i] = {}
    for j in json_data[i]:
        # SeoulMetro[i][(j["from"], j["to"])] = j["time"]
        SeoulMetro_list.append([j["from"], j["to"], j["time"]])

# ------------------------------------------------------------------
# 상행선
# ------------------------------------------------------------------
SeoulMetro_up = {}
for i in json_data:
    SeoulMetro_up[i] = {}
    for j in json_data[i]:
        SeoulMetro_up[i][j["to"]] = ([j["from"], j["time"]])
# ------------------------------------------------------------------
# 하행선
# ------------------------------------------------------------------
SeoulMetro_down = {}
for i in json_data:
    SeoulMetro_down[i] = {}
    for j in json_data[i]:
        SeoulMetro_down[i][j["from"]] = [j["to"], j["time"]]
# ------------------------------------------------------------------
input_vertex = []
# 기존 입력방식
# input_vertex = input().split(',')
for i in SeoulMetro_list:
    input_vertex.append(i[0])

input_vertex_1 = []
for i in range(len(SeoulMetro_list)):
    input_vertex_1.append(SeoulMetro_list[i][0])

for i in input_vertex[0:]:
    priority_Queue.append([i, maximum_value, 'x'])

for i in range(0, len(priority_Queue)):
    for j in range(0, 3):
        if priority_Queue[i][j] == in_start:
            priority_Queue[i][j + 1] = 0

for i in input_vertex[0:]:
    distance[i] = maximum_value

# for i in SeoulMetro:
#     input_all_vertex = input_all_vertex + len(SeoulMetro[i])

input_all_vertex = len(SeoulMetro_list)

for i in range(input_all_vertex):
    graph.insert(SeoulMetro_list[i][0], SeoulMetro_list[i][1], SeoulMetro_list[i][2])

distance[in_start] = 0
distance2[in_start] = [0]
'''
input_num_edges = input()
for i in range(int(input_num_edges)):
    input_data = input().split(',')
    graph.insert(input_data[0], input_data[1], input_data[2])
'''
# (윗줄) 여기까지가 input data 정리
if priority_Queue[0][0] == in_start:
    priority_Queue[0][2] = in_start

while len(priority_Queue) != 0:
    if distance[priority_Queue[0][0]] >= priority_Queue[0][1]:
        for i in range(len(input_vertex)):
            if graph.is_adjacent(priority_Queue[0][0], input_vertex[i]):
                if distance[input_vertex[i]] > min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i]))):
                    distance[input_vertex[i]] = min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i])))
                    priority_Queue.append([input_vertex[i], distance[input_vertex[i]], priority_Queue[0][0]])

        del priority_Queue[0]
        # priority_Queue.sort()
        priority_Queue = sorted(priority_Queue, key=lambda val: val[1])
    else:
        del priority_Queue[0]
        priority_Queue = sorted(priority_Queue, key=lambda val: val[1])

for i in SeoulMetro:
    input_all_vertex = input_all_vertex + len(SeoulMetro[i])


p_distance = sorted(distance.items())

mim_cost = maximum_value
for i in p_distance:
    if i[0] == in_end:
        print(in_start, "->", in_end, "=", i[1])
        min_cost = i[1]
        break

for i in range(len(p_distance)):
    print(p_distance[i][1])

cost_matrix2 = c(graph.cost_matrix)
app_path = ap()
print(app_path.out_dfs(in_start, in_end, input_vertex_1, cost_matrix2, min_cost))
# print sorted(distance, key=lambda t: t[1])

'''
for i in range(len(p_distance)):
    print p_distance[i][1]
'''