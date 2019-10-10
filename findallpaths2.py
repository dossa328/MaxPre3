import json
import time
from copy import deepcopy as c
from Graph import Graph
import numpy as np


def ppp(input_start, input_end, input_alpha):
    graph = Graph(undirected=True)
    start = time.time()

    with open('trans.json', 'r', encoding='UTF-8') as json_file:
        trans_data = json.load(json_file)
    with open('edges_fix.json', 'r', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
    with open('line.json', 'r', encoding='UTF-8') as line_file:
        line_data = json.load(line_file)

    SeoulMetroLine_translist = {}

    for i in line_data:
        for j in line_data[i]:
            SeoulMetroLine_translist[j+i] = i
            # SeoulMetroLine_list2.append([j+i, i])


    # split된 path 에 대해서 score를 계산한다.
    def score_sub(p_sub):
        cost = 0
        p_acc = 0.2 if p_sub[0] in trans_data["trans"] else 0.5

        for i in range(len(p_sub)):
            if p_sub[i] in trans_data["trans"]:
                cost = cost + 0.2 * cal_path_weight(i, p_sub)
            else:
                cost = cost + 0.5 * cal_path_weight(i, p_sub)
        return cost


    def cal_path_weight(idx, path):
        sum_path = 0
        for i in range(idx, len(path)-1):
            sum_path = sum_path + graph.get_cost(path[i], path[i+1])
        return sum_path


    def score_sub2(p_sub):
        cost = 0
        # for i in range(len(p_sub)):
        cost = cal_path_weight2(p_sub)
        #
        # if p_sub[i] in trans_data["trans"]:
        #     cost = cost + (pow(0.2, i)) * cal_path_weight2(i, p_sub)
        # else:
        #     cost = cost + (pow(0.5, i)) * cal_path_weight2(i, p_sub)
        return cost


    def cal_path_weight2(path):
        p_acc = 1
        for i in range(0, len(path)):
            if path[i] in trans_data["trans"]:
                p_acc = p_acc + ((((1 - p_acc) * i) * 0.2) + p_acc)
            else:
                p_acc = p_acc + ((((1 - p_acc) * i) * 0.5) + p_acc)
        return p_acc


    def split(path):
        paths = []
        out_cost = 0
        sv = []
        for i in range(len(path)):
            sv.append(path[i])
            # if i in trans_data["trans"] or i == in_end:
            if path[i] == in_end:
                out_cost = out_cost + score_sub(sv)
                # paths.append(score_sub(sv))
                sv = []

            elif not SeoulMetroLine_translist[path[i]] == SeoulMetroLine_translist[path[i+1]]:
                out_cost = out_cost + score_sub(sv)
                # paths.append(score_sub(sv))
                sv = []
        return out_cost


    count = 0
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
            if node not in path[0] and path[1]+w <= threshold:
                newpaths = find_all_paths(graph2, node, end, w, c(path))
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


    # print(find_all_paths(graph, 'A', 'D'))
    # print(find_shortest_path(graph.cost_matrix, in_start, in_end))
    in_start = input_start
    in_end = input_end
    dijkstra_result = np.load('Dijkstra_result.npy')
    dijkstra_dict = {}
    for r in dijkstra_result:
        dijkstra_dict[r[0]] = r[1]
    alpha = input_alpha
    threshold = float(dijkstra_dict[in_end]) * alpha
    output = find_all_paths(graph.cost_matrix, in_start, in_end)
    candidate_paths = []
    saved = []
    for p in output:
        # saved.append(split(p[0]))
        path_cost = split(p[0])
        p.append([(pow(p[1], -1)) * path_cost])
        candidate_paths.append(p)

    candidate_paths2 = sorted(candidate_paths, key=lambda cp: cp[2])

    for i in candidate_paths2:
        print(i)

    print('Count:', len(output))
    print("time :", time.time() - start)
