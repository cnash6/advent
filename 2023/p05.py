#!/usr/bin/env python

from utils import start_time, end_time

def do_it(fname: str):
    with open(fname, 'r') as f:
        inputs = f.read()
    
    sections = inputs.split("\n\n")
    seeds = sections[0].split(": ")[1].split()
    sections = [[tuple(int(z) for z in y.split()) for y in x.split(":\n")[1].split("\n")] for x in sections[1:]]

    min_loc = float('inf')
    for seed in seeds:
        curr = int(seed)
        for section in sections:
            for mapping in section:
                a,b = mapping[1], mapping[1]+mapping[2]
                if a <= curr < b:
                    curr = mapping[0] + (curr-a)
                    break
        min_loc = min(curr, min_loc)
    return min_loc

def do_it2(fname: str):
    with open(fname, 'r') as f:
        inputs = f.read()
    
    sections = inputs.split("\n\n")
    seeds = [int(x) for x in sections[0].split(": ")[1].split()]
    sections = [[tuple(int(z) for z in y.split()) for y in x.split(":\n")[1].split("\n")] for x in sections[1:]]

    min_loc = float('inf')

    for i in range(len(seeds)//2):
        print(f"{i}/{len(seeds)//2}")
        for seed in range(seeds[2*i], seeds[2*i]+seeds[2*i+1]):
            curr = int(seed)
            for section in sections:
                for mapping in section:
                    a,b = mapping[1], mapping[1]+mapping[2]
                    if a <= curr < b:
                        curr = mapping[0] + (curr-a)
                        break
            min_loc = min(curr, min_loc)
    return min_loc

def do_it2_different(fname):
    with open(fname, 'r') as f:
        inputs = f.read()   
    
    raw_sections = inputs.split("\n\n")
    seeds = [int(x) for x in raw_sections[0].split(": ")[1].split()]
    seeds = [range(seeds[2*i], seeds[2*i]+seeds[2*i+1]) for i in range(len(seeds)//2)]
    # print(seeds)

    raw_sections = [[y for y in x.split(":\n")[1].split("\n")] for x in raw_sections[1:]]
    for i in range(len(raw_sections)):
        for j in range(len(raw_sections[i])):
            m = raw_sections[i][j]
            m = [int(x) for x in m.split()]
            m = (range(m[1], m[1]+m[2]), m[0]-m[1])
            raw_sections[i][j] = m
        
    sections: list[list[tuple[range, int]]] = raw_sections
    # print(sections)

    for section in sections:
        print("seeds", seeds)
        for mapping in section:
            print("mapping", mapping)
            mapping_seeds = list(seeds)
            new_mapping_seeds = []
            for seed in mapping_seeds:
                print("seed -> mapping:", seed, mapping)
                if pre := range(seed.start, min(seed.stop, mapping[0].start)):
                    new_mapping_seeds.append(pre)
                if intersect := range(max(seed.start,mapping[0].start), min(seed.stop,mapping[0].stop)):
                    new_mapping_seeds.append(range(intersect.start+mapping[1], intersect.stop+mapping[1]))
                if post := range(max(seed.start, mapping[0].stop), seed.stop):
                    new_mapping_seeds.append(post)
            mapping_seeds = new_mapping_seeds
            print("all seeds mapped", new_mapping_seeds)
        print("Changed? ", (mapping_seeds != seeds))
        seeds = mapping_seeds
        print("new seeds", seeds, "\n\n")

    return seeds


        


# print(do_it("inputs/05.1"))
# print(do_it("inputs/05"))

print(do_it2_different("inputs/05.1"))
# s = start_time()
# print(do_it2_different("inputs/05"))
# print(end_time(s))
