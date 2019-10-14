from Graph import Graph


def cal_path_weight2(path, trans_data):
    p_acc = 0.2 if path[0] in trans_data["trans"] else 0.5
    expectation = p_acc * Graph.get_cost(path[0], path[1])

    for i in range(1, len(path)-1):

        p_i = 0.2 if path[i] in trans_data["trans"] else 0.5
        p_acc = p_acc + (1-p_acc) * p_i
        expectation = expectation + p_acc * Graph.get_cost(path[i], path[i+1])

    return expectation


path = ['고려대6', '안암6', '보문6', '창신6', '삼각지6']
trans_data = {}
trans_data["trans"] = ['창신', '보문']

if __name__ == '__main__':
    print(cal_path_weight2(path, trans_data))
