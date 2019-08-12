# -*- coding: utf-8 -*-
# (up line) use utf-8 coding
from Graph import Graph
from copy import deepcopy as c
from Allpathweight import ap
graph = Graph(undirected=False)
maximum_value = pow(2, 31)
input_way_edges = []
list_way_edges = {}
distance = {}
priority_Queue = []
distance2 = {}
in_start = 'E9'
in_end = 'F32'
# 밑에꺼 raw_input() 이었음..
input_vertex = input().split(',')
for i in input_vertex[0:]:
    priority_Queue.append([i, maximum_value, 'x'])

for i in range(0, len(priority_Queue)):
    for j in range(0, 3):
        if priority_Queue[i][j] == in_start:
            priority_Queue[i][j + 1] = 0

for i in input_vertex[0:]:
    distance[i] = maximum_value

distance[in_start] = 0
distance2[in_start] = [0]
input_num_edges = input()
for i in range(int(input_num_edges)):
    # 밑에꺼 raw_input() 이었음..
    input_data = input().split(',')
    graph.insert(input_data[0], input_data[1], input_data[2])

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


cost_matrix2 = c(graph.cost_matrix)
app_path = ap()
print(app_path.out_dfs(in_start, in_end, input_vertex, cost_matrix2))
# print sorted(distance, key=lambda t: t[1])


p_distance = sorted(distance.items())

'''
for i in range(len(p_distance)):
    print p_distance[i][1]
'''