#!/usr/bin/env python
# coding: utf-8

from collections import namedtuple, deque

Node = namedtuple('Node', 'x y keys p')

def print_graph(graph, node):
    printgraph = dict(graph)
    printgraph[(node.x, node.y)] = '@'
    min_x = min(x for x, _ in printgraph)
    min_y = min(y for _, y in printgraph)
    max_x = max(x for x, _ in printgraph)
    max_y = max(y for _, y in printgraph)
    print(node)
    print("\n".join(("".join(printgraph[(x, y)] for x in range(min_x, max_x + 1))) for y in range(min_y, max_y + 1)) + '\n')


def get_traversable_neighbors(node, graph):
    neighbors = []
    for d in [(1,0), (-1,0), (0,1), (0,-1)]:
        val = graph[(node.x+d[0], node.y+d[1])] 
        if val != '#' or (val not in node.keys and val.lower() in node.keys):
            neighbors.append(Node(node.x+d[0],  node.y+d[1], node.keys, node))
    return neighbors

def bfs(graph, goalfn, Q, discovered):
    if Q:
        node = Q.popleft()
        print_graph(graph, node)
        if goalfn(node):
            return node
        for neighbor in get_traversable_neighbors(node, graph):
            if neighbor not in discovered:
                discovered[neighbor] = True
                Q.append(neighbor)
    else: 
        return None
        
# Main      
f = open('assets/18.txt', 'r')
        
# Part 1

graph = {}
KEYS = []
start = None
for j,y in enumerate(f):
    for i,x in enumerate(y.rstrip()):
        graph[(i,j)] = x
        if x >= 'a' and x <= 'z':
            KEYS.append(x) 
        if x == '@':
            graph[(i,j)] = '.'
            start = Node(i,j,(), None)

print(KEYS)
print_graph(graph, start)

Q = deque()
discovered = {}

discovered[start] = True # This is wrong, will add new states to discovered at every 
                         # step because of Nodes have unique parents for each step.  Needs fix
Q.append(start)
goalfn = lambda x: sorted(list(x.keys)) == sorted(KEYS)

found = None
while Q:
    found = bfs(graph, goalfn, Q, discovered)
print(found)