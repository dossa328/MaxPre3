class Graph:
    def __init__(self, undirected):
        self.undirected = undirected
        self.cost_matrix = {}

    def insert(self, v_from, v_to, cost):

        if v_from not in self.cost_matrix:
            self.cost_matrix[v_from] = {}

        self.cost_matrix[v_from][v_to] = cost

        if self.undirected:
            v_from, v_to = v_to, v_from
            if v_from not in self.cost_matrix:
                self.cost_matrix[v_from] = {}

            self.cost_matrix[v_from][v_to] = cost

    def is_adjacent(self, v_from, v_to):
        if v_from not in self.cost_matrix:
            return False
        elif v_to not in self.cost_matrix[v_from]:
            return False
        else:
            return True

    def get_cost(self, v_from, v_to):
        if v_from not in self.cost_matrix:
            raise LookupError
        elif v_to not in self.cost_matrix[v_from]:
            raise LookupError
        return self.cost_matrix[v_from][v_to]
