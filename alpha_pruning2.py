import time
from copy import deepcopy as c
import numpy as np
import collections

import dijkstra

count = 0
def get_result(_metro, in_start, in_end, in_alpha):
    def score_sub2(p_sub, _metro):
        cost = cal_path_weight2(p_sub, _metro)
        # cost2 = score_sub(p_sub)
        return cost

    def cal_path_weight2(_path, _metro):

        _trans_list = _metro.trans_list
        _graph = _metro.graph

        p_acc = 0.2 if _path[0] in _trans_list["trans"] else 0.5
        if len(_path) >= 2:
            expectation = p_acc * _graph.get_cost(_path[0], _path[1])
        elif len(_path) < 2:
            expectation = p_acc * 0

        for i in range(1, len(_path) - 1):
            p_i = 0.2 if _path[i] in _trans_list["trans"] else 0.5
            p_acc = p_acc + (1 - p_acc) * p_i
            expectation = expectation + p_acc * _graph.get_cost(_path[i], _path[i + 1])

        return expectation

    # split된 path 에 대해서 score를 계산한다.
    def score_sub(p_sub, _metro):
        cost = 0
        p_remaining = 1
        for i in range(len(p_sub)):
            p_i = 0.2 if p_sub[i] in _metro.trans_list["trans"] else 0.5
            p_i = p_remaining * p_i
            p_remaining = p_remaining - p_i

            cost = cost + p_i * cal_path_weight(i, p_sub)
        return cost

    def cal_path_weight(idx, path, _metro):
        sum_path = 0
        for i in range(idx, len(path) - 1):
            sum_path = sum_path + _metro.graph.get_cost(path[i], path[i + 1])
        return sum_path

    def split(path, _metro):
        out_cost = 0
        sv = []
        for i in range(len(path)):
            sv.append(path[i])
            # if i in trans_list["trans"] or i == in_end:
            if path[i] == in_end:
                out_cost = out_cost + score_sub2(sv, _metro)
                # paths.append(score_sub(sv))
                sv = []

            elif not _metro.station_to_line[path[i]] == _metro.station_to_line[path[i + 1]]:
                out_cost = out_cost + score_sub2(sv, _metro)
                # paths.append(score_sub(sv))
                sv = []
        return out_cost

    # my origin
    # def find_all_paths(graph2, start, end, _threshold, weight=0,  path=[[], 0]):
    #     path[0], path[1] = path[0] + [start], path[1] + weight
    #     if start == end:
    #         return [path]
    #     paths = []
    #     for node, w in graph2[start].items():
    #         if node not in path[0] and path[1] + w <= _threshold:
    #             # if node not in deny:
    #             #     deny.append(node)
    #             newpaths = find_all_paths(graph2, node, end, _threshold, w, c(path))
    #             for newpath in newpaths:
    #                 paths.append(newpath)
    #     # print("add new paths : ", paths)
    #     return paths


    # python.org origin
    # def find_shortest_path(graph2, start, end, _threshold, weight=0,  path=[[], 0]):
    #     path[0], path[1] = path[0] + [start], path[1] + weight
    #     if start == end:
    #         return path
    #     if not start in graph2:
    #         return None
    #     shortest = None
    #     for node, w in graph2[start].items():
    #         if node not in path:
    #             newpath = find_shortest_path(graph2, node, end, path)
    #             if newpath:
    #                 if not shortest or len(newpath) < len(shortest):
    #                     shortest = newpath
    #     return shortest


    # python.org advanced
    # def find_shortest_path(graph2, start, end, _threshold, weight=0,  path=[[], 0]):
    #     dist = {start: [start]}
    #     q = collections.deque([start])
    #     while len(q):
    #         at = q.popleft()
    #         for next in graph2[at]:
    #             if next not in dist:
    #                 dist[next] = [dist[at], next]
    #                 q.append(next)
    #     return dist[end]

    # python.org origin all path
    def find_all_paths(graph2, start, end, path=[]):
        global count
        path = path + [start]
        if start == end:
            if path:
                if count % 1000 == 0:
                    print(count, ":", len(path))
                count = count + 1
            return [path]
        if not start in graph2:
            return []
        paths = []
        for node in graph2[start]:
            if node not in path:
                newpaths = find_all_paths(graph2, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    dijkstra.cal_dists(in_start)
    dijkstra_result = np.load('Dijkstra_result.npy')
    dijkstra_dict = {destination: dist for destination, dist in dijkstra_result}

    threshold = float(dijkstra_dict[in_end]) * in_alpha

    # candidate_paths = find_all_paths(_metro.graph.cost_matrix, in_start, in_end, threshold)
    # candidate_paths = find_shortest_path(_metro.graph.cost_matrix, in_start, in_end, threshold)
    # to origin py_all_path
    candidate_paths = find_all_paths(_metro.graph.cost_matrix, in_start, in_end)

    output = []
    for p in candidate_paths:
        # saved.append(split(p[0]))
        path_cost = split(p[0], _metro)
        # p.append([(pow(p[1], -1)) * path_cost])
        p.append(path_cost)
        output.append(p)

    # sort , 높은 점수만
    # output = sorted(output, key=lambda cp: -cp[2])
    # 가장 짧은 거리만
    output = sorted(output, key=lambda cp: -cp[1])
    return output[0]

    # return sorted(output, key=lambda cp: -cp[2])