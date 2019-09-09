maxint = pow(2, 31)


class Vertex:
    def __init__(self, c):
        self.c = c
        self.d = maxint
        self.next = {}

    def add_next(self, next_v, w):
        self.next[next_v] = w

    def relax(self, u):
        w = u.next[self]
        if self.d > u.d + w:
            self.d = u.d + w


C = raw_input().split(',')
source = Vertex(C[0])
source.d = 0
vertices = {C[0]: source}
for c in C[1:]:
    vertices[c] = Vertex(c)
num_edges = input()
for _ in range(num_edges):
    edge = raw_input().split(',')
    u = vertices[edge[0]]
    v = vertices[edge[1]]
    w = int(edge[2])
    u.add_next(v, w)


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
    min_heap = build_min_heap(list(V.values()))
    while len(min_heap) > 0:
        u = min_heap[0]
        S.append(u)
        v_list = sorted(u.next.keys(), key=lambda v: v.c)
        for v in v_list:
            v.relax(u)
        min_heap = build_min_heap(min_heap[1:])
    return sorted(S, key=lambda v: v.c)


result = dijkstra(vertices)
for v in result:
    print(v.d)