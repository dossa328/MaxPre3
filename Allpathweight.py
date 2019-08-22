from copy import deepcopy as deepcopy
from Graph import Graph
graph = Graph(undirected=False)


class ap:
    def __init__(self, lines):
        self.lines = lines
        self.visit = list()
        self.stack = list()
        self.all_path = {}
        self.candidate_path = []
        self.out_candidate_path = list()
        self.cc = 0
        self.can_path_out = []
        self.cost_matrix2 = {}
        self.min_cost = 0
        self.cc2 = 0

    def is_adjacent2(self, v_from, v_to):
        if v_from not in self.cost_matrix2:
            return False
        elif v_to not in self.cost_matrix2[v_from]:
            return False
        else:
            return True

    def is_sameline(self, before, after):
        for i in self.lines[0]:
            if before == i:
                before_key = i
            if after == i:
                after_key = i

        if before_key == after_key:
            return True
        else:
            return False

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
                self.cc2 = self.cc2 + int(self.get_cost(it, self.visit[-1]))
                if it not in self.visit:
                    if self.cc2 > self.min_cost:
                        break
                    self.cal_dfs(it, end, input_vertex)
                    self.visit.remove(it)
                    self.cc2 = 0
        self.stack.pop()

    def out_dfs(self, start, end, input_vertex, cost_matrix2, min_cost):
        self.cost_matrix2 = cost_matrix2
        self.min_cost = min_cost
        input_vertex = list(set(input_vertex))
        self.cal_dfs(start, end, input_vertex)
        for i in range(len(self.candidate_path)):
            cc = 0
            for j in range(len(self.candidate_path[i]) - 1):
                    cc = cc + int(self.get_cost(self.candidate_path[i][j], self.candidate_path[i][j + 1]))
                    if self.candidate_path[i][j] == "공덕":
                        cc = cc + 1.016667
                    if self.candidate_path[i][j] == "청구":
                        cc = cc + 1.45

            if cc > self.min_cost*1.1:
                pass
            else:
                self.candidate_path[i].append(cc)
                self.out_candidate_path.append(self.candidate_path[i])

        return self.out_candidate_path


