import time

def check_progress(i, n):
    if i % (n//100) == 0:
        print("..." + str(i // (n//100)) + "%", end="\r")

def aocin(fname) -> list[str]:
    with open(fname, 'r') as f:
        return [x.strip() for x in f.readlines()]

def togrid(inputs):
    return [[y for y in x.strip()] for x in inputs]

def start_time():
        return time.time()

def end_time(s):
        print("--- %s seconds ---" % (time.time() - s))

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
