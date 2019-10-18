import json
import time
import numpy as np

start = time.time()


def cal_dists(input_start_v, input_end_v):
    paths = []
    maxint = pow(2, 31)

    with open('edges_fix.json', 'r', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)

    with open('line.json', 'r', encoding='UTF-8') as line_file:
        line_data = json.load(line_file)

    # transline = []
    # print(line_data.keys())

    SeoulMetro = {}
    SeoulMetroLine = {}
    SeoulMetro_list = []
    SeoulMetroLine_list = []
    SeoulMetroLine_list2 = []
    for i in json_data:
        # SeoulMetro[i] = {}
        if not i == "Trans":
            for j in json_data[i]:
                SeoulMetro_list.append([j["from"] + i, j["to"] + i, j["time"]])
                SeoulMetro_list.append([j["to"] + i, j["from"] + i, j["time"]])
        elif i == "Trans":
            for j in json_data[i]:
                SeoulMetro_list.append([j["from"], j["to"], j["time"]])
                SeoulMetro_list.append([j["to"], j["from"], j["time"]])

    for i in line_data:
        for j in line_data[i]:
            SeoulMetroLine_list.append(j + i)

    class Vertex:
        def __init__(self, c):
            self.c = c
            self.d = maxint
            self.path = []
            self.next = {}

        def add_next(self, next_v, w):
            self.next[next_v] = w

        def relax(self, u):
            w = u.next[self]
            if self.d > u.d + w:
                self.d = u.d + w
                # if not u.path:
                #     self.path.append(u.c)
                # if u.path:
                #     self.path.extend(u.path)
                #     self.path.append(u.c)

    def build_min_heap(A):
        def min_heapify(A, i):
            l = 2 * i + 1
            r = 2 * i + 2
            size = len(A)
            if l < size and A[l].d < A[i].d:
                smallest = l
            else:
                smallest = i
            if r < size and A[r].d < A[smallest].d:
                smallest = r
            if smallest != i:
                temp = A[i]
                A[i] = A[smallest]
                A[smallest] = temp
                return min_heapify(A, smallest)
            else:
                return A

        for i in range(len(A) // 2 - 1, -1, -1):
            A = min_heapify(A, i)
        return A

    def dijkstra(V):
        S = []
        S_path = {}
        min_heap = build_min_heap(list(V.values()))
        # S_path[min_heap[0].c] = min_heap[0].c
        while len(min_heap) > 0:
            S_add = []
            u = min_heap[0]
            S.append(u)
            for S_s in S:
                S_add.append(S_s.c)
            S_path[u.c] = S_add
            v_list = sorted(u.next.keys(), key=lambda v: v.c)
            for v in v_list:
                v.relax(u)
            min_heap = build_min_heap(min_heap[1:])
        return sorted(S, key=lambda v: v.c), S_path

    in_start = input_start_v
    # C = input().split(',')
    # source = Vertex(SeoulMetroLine_list[0])
    source = Vertex(in_start)
    source.d = 0
    vertices = {in_start: source}
    for c in SeoulMetroLine_list[0:]:
        if not c == in_start:
            vertices[c] = Vertex(c)
    num_edges = len(SeoulMetro_list)
    for i in range(num_edges):
        edge = SeoulMetro_list[i]
        u = vertices[edge[0]]
        v = vertices[edge[1]]
        w = int(edge[2])
        u.add_next(v, w)

    result, result_path = dijkstra(vertices)
    # print("time :", time.time() - start)
    # print(SeoulMetroLine_list)

    result_tuples = []
    result_tuples_for_dijk_score = []

    reresult = []
    for v in result:
        paths.append(v.path)

    for vv in paths:
        if not vv:
            pass
        elif input_end_v == vv[-1]:
            reresult.append(vv)

    return reresult
    # for v in result:
    #     result_tuples.append((v.c, v.d))

        # np.save('Dijkstra_result', np.array(result_tuples))
        # print("time :", time.time() - start)
