def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


graph = {'A': {'B', 'C'},
         'B': {'C', 'D'},
         'C': {'D'},
         'D': {'C'},
         'E': {'F'},
         'F': {'C'}}

print(find_all_paths(graph, 'A', 'D'))
