# !/usr/bin/env python

def sum_aggs(tree):
    children = tree[0]
    metas = tree[1]
    score = 0
    values = []
    leftovers = tree[2:]

    for i in range(children):
        c_score, c_value, leftovers = sum_aggs(leftovers)
        score += c_score
        values.append(c_value)

    score += sum(leftovers[:metas])

    if children > 0:
        return (score, sum(values[x - 1] for x in leftovers[:metas] if x <= len(values)), leftovers[metas:])
    return (score, sum(leftovers[:metas]), leftovers[metas:])
    
    
if __name__ == '__main__':
    f = open('assets/08.txt', 'r')
    
    #  Part 1
    data = [int(x) for x in f.read().strip().split(' ')]
    print(sum_aggs(data))