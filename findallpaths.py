import json
from copy import deepcopy as c
from Graph import Graph
import numpy as np
graph = Graph(undirected=True)

in_start = '목동5'
in_end = '안암6'
count = 0
with open('edges_fix.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)


newpaths2 = {}
SeoulMetro = {}
SeoulMetroLine = {}
SeoulMetro_list = []
SeoulMetroLine_list = []
for i in json_data:
    # SeoulMetro[i] = {}
    if not i == "Trans":
        for j in json_data[i]:
            SeoulMetro_list.append([j["from"]+i, j["to"]+i, j["time"]])
            SeoulMetro_list.append([j["to"]+i, j["from"]+i, j["time"]])
    elif i == "Trans":
        for j in json_data[i]:
            SeoulMetro_list.append([j["from"], j["to"], j["time"]])
            SeoulMetro_list.append([j["to"], j["from"], j["time"]])


for i in SeoulMetro_list:
    graph.insert(i[0], i[1], i[2])


def find_all_paths(graph2, start, end, weight=0, path=[[], 0]):
    path[0], path[1] = path[0]+[start], path[1]+weight
    if start == end:
        return [path]
    paths = []
    for node, w in graph2[start].items():
        if node not in path[0] and path[1]+w < threshold:
            newpaths = find_all_paths(graph2, node, end, w, c(path))
            for newpath in newpaths:
                paths.append(newpath)
    return paths


#
# graph = {'A': {'B': 4, 'C': 5},
#          'B': {'C': 6, 'D': 5},
#          'C': {'D': 7},
#          'D': {'C': 2},
#          'E': {'F': 8},
#          'F': {'C': 6}}


#print(find_all_paths(graph, 'A', 'D'))
# print(find_shortest_path(graph.cost_matrix, in_start, in_end))

dijkstra_result = np.load('Dijkstra_result.npy')
dijkstra_dict = {}
for r in dijkstra_result:
    dijkstra_dict[r[0]] = r[1]
alpha = 1.0
threshold = float(dijkstra_dict[in_end]) * alpha
print(threshold)
print(find_all_paths(graph.cost_matrix, in_start, in_end))
