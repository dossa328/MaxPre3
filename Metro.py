import json
from Graph import Graph


class Metro(object):
    def __init__(self):

        self.graph = Graph(undirected=True)

        with open('trans.json', 'r', encoding='UTF-8') as json_file:
            self.trans_list = json.load(json_file)
        with open('edges_fix.json', 'r', encoding='UTF-8') as json_file:
            self.dist_1hop_dict = json.load(json_file)
        with open('line.json', 'r', encoding='UTF-8') as line_file:
            self.line_to_stations = json.load(line_file)

        self.station_to_line = {}

        for i in self.line_to_stations:
            for j in self.line_to_stations[i]:
                self.station_to_line[j + i] = i

        self.SeoulMetro_list = []

        for i in self.dist_1hop_dict:
            # SeoulMetro[i] = {}
            if not i == "Trans":
                for j in self.dist_1hop_dict[i]:
                    self.SeoulMetro_list.append([j["from"] + i, j["to"] + i, j["time"]])
                    self.SeoulMetro_list.append([j["to"] + i, j["from"] + i, j["time"]])
            elif i == "Trans":
                for j in self.dist_1hop_dict[i]:
                    self.SeoulMetro_list.append([j["from"], j["to"], j["time"]])
                    self.SeoulMetro_list.append([j["to"], j["from"], j["time"]])

        for i in self.SeoulMetro_list:
            self.graph.insert(i[0], i[1], i[2])
