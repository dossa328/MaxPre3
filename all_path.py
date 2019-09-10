# Python program to print all paths from a source to destination.
from collections import defaultdict

import json
import time
start = time.time()


# This class represents a directed graph
# using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = 'True'
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == 'False':
                    self.printAllPathsUtil(i, d, visited, path)

                    # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d, SeoulMetroLine_list):
        vi = SeoulMetroLine_list
        visited = {}
        # Mark all the vertices as not visited
        for ii in vi:
            visited[ii] = 'False'
        # visited[SeoulMetroLine_list] = [False] * self.V

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
        # Create a graph given in the above diagram


SeoulMetro = {}
SeoulMetroLine = {}
SeoulMetro_list = []
SeoulMetroLine_list = []

with open('edges_fix.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)

line_list = []
for i in line_data:
    # SeoulMetroLine[i] = {}
    for j in line_data[i]:
        SeoulMetroLine_list.append(j+i)

for i in line_data:
    for j in line_data[i]:
        line_list.append(j)


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


g = Graph(719)
for i in SeoulMetro_list:
    g.addEdge(i[0], i[1])

s = "공덕5"
d = "마포5"
print("Following are all different paths from", s, "to", d)
g.printAllPaths(s, d, SeoulMetroLine_list)

# print(g.graph)
