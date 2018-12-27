# !/usr/bin/env python
from collections import namedtuple

def print_track(track, carts):
    t = [row[:] for row in track]
    # print("".join(["".join(x)+"\n" for x in t]))
    for c in carts:
        # print(c)
        t[c.y][c.x] = c.d
    print("".join(["".join(x)+"\n" for x in t]))

def turn_left(d):
    if d == '<':
        return 'v'
    if d == '>':
        return '^'
    if d == '^':
        return '<'
    if d == 'v':
        return '>'

def turn_right(d):
    if d == '<':
        return '^'
    if d == '>':
        return 'v'
    if d == '^':
        return '>'
    if d == 'v':
        return '<'

if __name__ == '__main__':
    f = open('assets/13.txt', 'r')
    
    #  Part 1
    track = [[y for y in x[:-1]] for x in f]
    Cart = namedtuple('cart', 'x y d tseq')
    Point = namedtuple('point', 'x y')

    next_turn = {'l': 's', 's': 'r', 'r': 'l'}

    carts = []
    for y in range(len(track)):
        for x in range(len(track[y])):
            if track[y][x] in ['<', '>', '^', 'v']:
                carts.append(Cart(x, y, track[y][x], 'l'))
                track[y][x] = '-' if track[y][x] in ['<', '>'] else '|'

    # print_track(track, carts)
    while len(carts) > 1:
        carts = sorted(carts, key=lambda x: (x.y, x.x))
        ci = 0
        while ci < len(carts):
            cart = carts[ci]
            n = None
            d = cart.d
            if d == '>':
                n = Point(cart.x+1, cart.y)
            elif d == '<':
                n = Point(cart.x-1, cart.y)
            elif d == '^':
                n = Point(cart.x, cart.y-1)
            elif d == 'v':
                n = Point(cart.x, cart.y+1)

            conflict = list(filter(lambda x: x.x == n.x and x.y == n.y, carts))
            if len(conflict) > 0:
                print(f'Crash! {(n.x, n.y)}')
                ci = ci - 1 if carts.index(conflict[0]) < carts.index(cart) else ci 
                carts.remove(cart)
                carts.remove(conflict[0])
            else:
                newd = d
                ntseq = cart.tseq
                if track[n.y][n.x] == '/':
                    if d == '>':
                        newd = '^'
                    elif d == '<':
                        newd = 'v'
                    elif d == '^':
                        newd = '>'
                    elif d == 'v':
                        newd = '<'
                    cart = Cart(n.x, n.y, newd, cart.tseq)
                elif track[n.y][n.x] == '\\':
                    if d == '>':
                        newd = 'v'
                    elif d == '<':
                        newd = '^'
                    elif d == '^':
                        newd = '<'
                    elif d == 'v':
                        newd = '>'
                    cart = Cart(n.x, n.y, newd, cart.tseq)
                elif track[n.y][n.x] == '+':
                    if cart.tseq == 'l':
                        newd = turn_left(d)
                    elif cart.tseq == 'r':
                        newd = turn_right(d)
                    ntseq = next_turn[cart.tseq]
                carts[ci] = Cart(n.x, n.y, newd, ntseq)
                ci+=1
        # print_track(track, carts)
    print(carts[0])
