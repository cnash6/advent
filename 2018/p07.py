# !/usr/bin/env python
from collections import defaultdict
import string

def print_the_thing(timer, worked, workers, done):
    to_print = str(timer) + "\t"
    for i in range(workers):
        to_print = to_print + worked[i] if i < len(worked) else to_print + '.'
        to_print = to_print + "\t"
    to_print = to_print + done
    return to_print

    print(f'{timer}  {"   ".join(worked)}   {done}')

if __name__ == '__main__':
    f = open('assets/07.txt', 'r')
    
    #  Part 1
    # input_deps = [(x[5], x[36]) for x in f]


    # deps = defaultdict(list)
    # nodes = []
    # for input_dep in input_deps:
    #     deps[input_dep[1]].append(input_dep[0])
    #     if input_dep[1] not in nodes:
    #         nodes.append(input_dep[1])
    #     if input_dep[0] not in nodes:
    #         nodes.append(input_dep[0])

    # nodes = sorted(nodes)

    # sol = ""
    # while(len(nodes)) > 0:
    #     for node in nodes:
    #         if not any(dep in nodes for dep in deps[node]):
    #             sol = sol + node
    #             nodes.remove(node)
    #             break

    # print(sol)

    #  Part 2

    input_deps = [(x[5], x[36]) for x in f]
    WORKERS = 5
    DELAY = 60


    deps = defaultdict(list)
    nodes = defaultdict(int)
    for input_dep in input_deps:
        deps[input_dep[1]].append(input_dep[0])
        if input_dep[1] not in nodes:
            nodes[input_dep[1]] = 0
        if input_dep[0] not in nodes:
            nodes[input_dep[0]] = 0

    for node in sorted(nodes):
        print(node)
        print(deps[node])

    timer = 0
    done = ""
    working = []
    while(len(list(nodes))) > 0:
        # print(f'TIME: {timer}')
        # print(nodes)
        for node in list(nodes):
            if nodes[node] >= (DELAY + string.ascii_uppercase.index(node)+1):
                # print(f'{node} is done')
                done += node
                del nodes[node]
                working.remove(node)
        for worker in working:
            nodes[worker] += 1 
        for node in sorted(list(nodes)):
            if len(working) >= WORKERS:
                break
            if not any(dep in nodes for dep in deps[node]) and node not in working:
                working.append(node)
                nodes[node] += 1


        print(print_the_thing(timer, working, WORKERS, done))
        timer += 1

    print(done)
    print(timer-1)


