def check_progress(i, n):
    if i % (n//100) == 0:
        print("..." + str(i // (n//100)) + "%", end="\r")

def aocin(fname):
    return open(fname, 'r').readlines() if len(open(fname, 'r').readlines()) > 1 else open(fname, 'r').read()

def togrid(inputs):
    return [[y for y in x.strip()] for x in inputs]