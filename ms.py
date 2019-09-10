import json
import time
start = time.time()
import numpy as np

maxint = pow(2, 31)

with open('edges_fix.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)

in_start = '불광6'
in_end = '고려대'
alpha = maxint

# transline = []
# print(line_data.keys())

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

for i in line_data:
    # SeoulMetroLine[i] = {}
    for j in line_data[i]:
        SeoulMetroLine_list.append(j+i)

print(len(SeoulMetroLine_list))


class Path:
    def __init__(self, init_d, init_p=None):
        self.p = [] if init_p is None else init_p
        self.d = init_d

    def extended(self, new_c, new_w):
        p = self.p + [new_c]
        d = self.d + new_w
        return Path(d, p)

    def __str__(self):
        s = "Cost:" + str(self.d) + "/ Path: "
        for node in self.p:
            s += node + ","
        return s


class Vertex:
    def __init__(self, c):
        self.c = c
        # d = set of tuples
        # each tuple = { path , d }
        self.P = [Path(maxint)]
        self.next = {}

    def add_next(self, next_v, w):
        self.next[next_v] = w

    def p_min(self):
        return sorted(self.P, key=lambda p: p.d)[0]

    def relax(self, u):
        w = u.next[self]
        cand_paths = []
        for p in u.P:
            cand_paths.append(p.extended(self.c, w))
        for cand_path in cand_paths:
            p_min = self.p_min()
            if p_min.d * alpha > cand_path.d:
                self.P.append(cand_path)
                if p_min.d > cand_path.d:
                    for p in self.P:
                        if p.d > alpha * cand_path.d:
                            self.P.remove(p)


# C = input().split(',')
# source = Vertex(SeoulMetroLine_list[0])
source = Vertex(in_start)
source.P = [Path(0, [in_start])]
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


def dijkstra(V):
    S = []
    V_sorted = sorted(list(V.values()), key=lambda v: v.p_min().d)
    while len(V_sorted) > 0:
        u = V_sorted[0]
        S.append(u)
        v_list = sorted(u.next.keys(), key=lambda v: v.c)
        for v in v_list:
            v.relax(u)
        V_sorted = sorted(V_sorted[1:], key=lambda v: v.p_min().d)
    return sorted(S, key=lambda v: v.c)


result = dijkstra(vertices)
print("time :", time.time() - start)
# print(SeoulMetroLine_list)
destinations = ['독바위6', '불광3']
for v in result:
    if True:
        print(v.c, len(v.P))
        for p in v.P:
            print(p)


