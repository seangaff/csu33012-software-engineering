import sys

class DAG:
    def __init__(self):
        self.graph = {}

    def add_node(self, node, graph={}):
        if not graph:
            graph = self.graph

        if node in graph:
            return False
        graph[node] = []

    def add_edge(self, n1, n2, graph={}):
        if not graph:
            graph = self.graph
        if n1 in graph and n2 in graph:
            graph[n1].append(n2)
            return True
        return False

def findLCA(graph, n1, n2):
    if not isAcyclic(graph):
        return None
    global n1_list
    global n2_list
    n1_list = []
    n2_list = []
    for node in graph:
        dfs([node], graph, node, 1, n1)
        dfs([node], graph, node, 2, n2)

    min_dist = sys.maxsize
    for x in n1_list:
        for y in n2_list:
            dist = 0
            for i, nX in enumerate(reversed(x)):
                dist = i
                for nY in reversed(y):
                    if nX == nY and dist < min_dist:
                        lca = nY
                        min_dist = dist
                        return lca
                    dist += 1
    return None

def dfs(node_list, graph, node, i, terminal_node):
    if node == terminal_node:
        if i == 1:
            n1_list.append(node_list[:])
        elif i == 2:
            n2_list.append(node_list[:])
        return True
    if not graph[node]:
        return True
    else:
        for x in graph[node]:
            node_list.append(x)
            dfs(node_list, graph, x, i, terminal_node)
            node_list.remove(x)
        return True

def isAcyclic(graph):
    for node in graph:
        if not isAcyclicRecursive([node], graph, node):
            return False

    return True

def isAcyclicRecursive(node_list, graph, node):
    if not graph[node]:
        return True
    else:
        for x in graph[node]:
            if x not in node_list:
                node_list.append(x)
                if not isAcyclicRecursive(node_list, graph, x):
                    return False
                node_list.remove(x)
            else:
                return False
        return True