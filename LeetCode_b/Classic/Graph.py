# -*- coding:UTF-8 -*-

def find_one_path(graph, start, end, path=[]):
    """
    返回任意一条路径
    :param graph:
    :param start:
    :param end:
    :param path:
    :return:
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_one_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def find_shortest_path(graph, start, end, path=[]):
    """
    返回最短路径
    :param graph:
    :param start:
    :param end:
    :param path:
    :return:
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_all_paths_dfs(graph, start, end, path=[]):
    """
    返回所有路径DFS
    :param graph:
    :param start:
    :param end:
    :param path:
    :return:
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths_dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_all_paths_bfs(graph, start, end):
    """
    返回所有路径BFS
    :param graph:
    :param start:
    :param end:
    :return:
    """
    paths = []
    todo = [[start, [start]]]
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            if next_node in path:
                continue
            elif next_node == end:
                paths.append(path + [next_node])
            else:
                todo.append([next_node, path + [next_node]])
    return paths


def recursive_dfs(graph, start, path=[]):
    """
    dfs遍历 递归形式
    :param graph:
    :param start:
    :param path:
    :return:
    """
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = recursive_dfs(graph, node, path)
    return path


def iterative_dfs(graph, start, path=[]):
    '''
    dfs遍历 非递归形式
    :param graph:
    :param start:
    :param path:
    :return:
    '''
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
            path = path + [v]
            q = graph[v] + q
    return path


def iterative_bfs(graph, start, path=[]):
    '''
    bfs遍历 非递归形式
    :param graph:
    :param start:
    :param path:
    :return:
    '''
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
            path = path + [v]
            q = q + graph[v]
    return path


if __name__ == '__main__':
    '''
       +---- A
       |   /   \
       |  B--D--C
       |   \ | /
       +---- E
    '''
    graph = {'A': ['B', 'C'],
             'B': ['D', 'E'],
             'C': ['D', 'E'],
             'D': ['E'],
             'E': ['A']}
    print('recursive dfs: ', recursive_dfs(graph, 'A'))
    print('iterative dfs: ', iterative_dfs(graph, 'A'))
    print('iterative bfs: ', iterative_bfs(graph, 'A'))

    print("##" * 20)

    print('find_one_path: ', find_one_path(graph, 'A', 'E'))
    print('find_shortest_path: ', find_shortest_path(graph, 'A', 'E'))
    print('find_all_paths dfs: ', find_all_paths_dfs(graph, 'A', 'E'))

    print("##" * 20)

    for path in find_all_paths_bfs(graph, 'A', 'E'):
        print(path)
