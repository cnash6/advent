# !/usr/bin/env python
from collections import deque
from utils import check_progress

if __name__ == '__main__':
    N = '652601'
    t = str(N)

    recipes = '37'
    e1 = 0
    e2 = 1
    
    searching = True
    # while len(recipes) < N + 10:
    while t not in recipes[-(len(t)+1):]:
        recipes+= str(int(recipes[e1]) + int(recipes[e2]))
        e1 = (e1 + int(recipes[e1]) + 1) % len(recipes)
        e2 = (e2 + int(recipes[e2]) + 1) % len(recipes)
        

    # print(recipes[int(t):int(t)+10])
    print(recipes.index(t))
