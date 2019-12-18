#!/usr/bin/env python
# coding: utf-8

import time
from tkinter import *
from shared.intcode import *
import curses

def build_board(raw):
    pixels = {(raw[i], raw[i+1]) : raw[i+2] for i in range(0, len(raw)-1, 3)}
    return [[pixels[(x,y)] for x in range(max([p[0] for p in pixels.keys()])+1)] for y in range(max([p[1] for p in pixels.keys()])+1)]

def draw_cell(stdscr, board, score):
    time.sleep(0.001)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)

    stdscr.addstr(0, 0, f'{score}\n')
    ch = tiles.get(cell[2])
    stdscr.addstr(cell[1]+1, cell[0], ch[0], curses.color_pair(ch[1]))
    stdscr.refresh()

# Main      
f = open('assets/13.txt', 'r')
intcode = [int(x) for x in f.read().rstrip().split(',')]

# Part 1
c = Computer(intcode[:])
c.run_program()
board = build_board(c.outputs)
print(len([x for y in board for x in y if x == 2]))

# Part 2
tiles = {
    0: (' ', 1),
    1: (' ', 2),
    2: (' ', 3),
    3: ('_', 4),
    4: ('O', 5)
}

X, Y = 44, 20
board = [[0 for x in range(X)] for y in range(Y)]
c = Computer([2] + intcode[1:])
score = 0
playing = False
ball = (0,0)
paddle = (0,0)
i = 0

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()

while "KILL" not in c.outputs:
    i+=1
    c.tick()
    if len(c.outputs) > 2:
        cell = c.outputs[:3]
        if cell[0] == -1:
            playing = True
            score = cell[2]
        else:
            if cell[2] == 3:
                paddle = (cell[0], cell[1])
            if cell[2] == 4:
                ball = (cell[0], cell[1])
                if ball[0] > paddle[0]:
                    c.inputs.append(1)
                elif ball[0] < paddle[0]:
                    c.inputs.append(-1)
                else:c.inputs.append(0)
            draw_cell(stdscr, cell, f'{score}\tb:{ball} p:{paddle}')
        
        c.outputs = c.outputs[3:]

curses.nocbreak()
curses.echo()
curses.endwin()

print(score)        

# In[ ]:




