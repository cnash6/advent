import time

def check_progress(i, n):
    if i % (n//100) == 0:
        print("..." + str(i // (n//100)) + "%", end="\r")

def aocin(fname):
    return [x.strip() for x in open(fname, 'r').readlines()] if len(open(fname, 'r').readlines()) > 1 else open(fname, 'r').read()

def togrid(inputs):
    return [[y for y in x.strip()] for x in inputs]

def start_time():
        return time.time()

def end_time(s):
        print("--- %s seconds ---" % (time.time() - s))
