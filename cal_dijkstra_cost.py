import numpy as np


def dijkstra_get_cost(_metro, in_start, in_end):

    # dijkstra_dict = {destination: dist for destination, paths, dist in dijkstra_result}

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

    dijkstra_result = np.load('Dijkstra_result_for_dijk_score.npy', allow_pickle=True)
    print("Dijkstra_cal_result : ", dijkstra_result[0][2], "::", split(dijkstra_result[0][2], _metro))
