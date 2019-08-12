from copy import deepcopy as deepcopy
from Graph import Graph
graph = Graph(undirected=False)


class ap:
    def __init__(self):
        self.visit = list()
        self.stack = list()
        self.all_path = {}
        self.candidate_path = []
        self.cc = 0
        self.can_path_out = []
        self.cost_matrix2 = {}

    def is_adjacent2(self, v_from, v_to):
        if v_from not in self.cost_matrix2:
            return False
        elif v_to not in self.cost_matrix2[v_from]:
            return False
        else:
            return True

    def get_cost(self, v_from, v_to):
        if v_from not in self.cost_matrix2:
            raise LookupError
        elif v_to not in self.cost_matrix2[v_from]:
            raise LookupError
        return self.cost_matrix2[v_from][v_to]

    def cal_dfs(self, start, end, input_vertex):
        self.visit.append(start)
        self.stack.append(start)
        if start == end:
            self.all_path[start] = deepcopy(self.stack)
            self.candidate_path.extend((self.all_path.values()))
            self.stack.pop()
            return self.candidate_path
        for it in input_vertex:
            if self.is_adjacent2(start, it):
                if it not in self.visit:
                    self.cal_dfs(it, end, input_vertex)
                    self.visit.remove(it)

        self.stack.pop()

    def out_dfs(self, start, end, input_vertex, cost_matrix2):
        self.cost_matrix2 = cost_matrix2
        self.cal_dfs(start, end, input_vertex)
        for i in range(len(self.candidate_path)):
            cc = 0
            for j in range(len(self.candidate_path[i]) - 1):
                cc = cc + int(self.get_cost(self.candidate_path[i][j], self.candidate_path[i][j + 1]))
            self.candidate_path[i].append(cc)

        return self.candidate_path
