#!/usr/bin/env python
# coding: utf-8

import time
from shared.intcode import *
import curses
from collections import deque

# def print_hull(panels):
#     maxx = -float('inf')
#     minx = float('inf')
#     maxy = -float('inf')
#     miny = float('inf')
#     for key in panels.keys():
#         if key[0] > maxx:
#             maxx = key[0]
#         if key[0] < minx:
#             minx = key[0]
#         if key[1] > maxy:
#             maxy = key[1]
#         if key[1] < miny:
#             miny = key[1]
            
#     for y in range(maxy, miny-1, -1):
#         for x in range(minx, maxx+1):
#             if panels.get((x,y), 0):
#                 cprint('▀', 'white', 'on_white', end='')
#             else: 
#                 cprint('▀', 'grey', 'on_grey', end='')
#         print()

def print_maze(stdscr):
    maxx = -float('inf')
    minx = float('inf')
    maxy = -float('inf')
    miny = float('inf')
    for key in maze.keys():
        if key[0] > maxx:
            maxx = key[0]+1
        if key[0] < minx:
            minx = key[0]-1
        if key[1] > maxy:
            maxy = key[1]+1
        if key[1] < miny:
            miny = key[1]-1
    stdscr.addstr(0, 0, str(robot), curses.color_pair(5))
    for y in range(maxy, miny-1, -1):
        for x in range(minx, maxx+1):
            v1 = maze.get((x,y), {'block': -1})['block']
            v2 = ccolors.get(v1)
            stdscr.addstr(y+abs(miny)+2, x+abs(minx)+2, ' ', v2)
            stdscr.refresh()
    stdscr.addstr(robot.y+abs(miny)+2, robot.x+abs(minx)+2, '*', curses.color_pair(4))
    stdscr.refresh()
    # stdscr.getkey()
    # time.sleep(0.005)



#     stdscr.addstr(0, 0, f'{score}\n')
#     ch = tiles.get(cell[2])
#     stdscr.addstr(cell[1]+1, cell[0], ch[0], curses.color_pair(ch[1]))
#     stdscr.refresh()

class Robot:
    def __init__(self, _intcode):
        self.x = 0
        self.y = 0
        self.comp = Computer(_intcode)
    
    def __str__(self):
        return f'R({self.x}) {self.y})'
        # return f'R({self.x}, {self.y}\t{self.comp.out_log})'


def get_next_untried(possible):
    n = moves[-1] if moves else 'N'
    if n in possible:
        return n
    if left[n] in possible:
        return left[n]
    if right[n] in possible:
        return right[n]
    if possible:
        return possible[0]
    return None

def explore_direction(direction):
    robot.comp.inputs.append({'N': 1, 'S': 2, 'W': 3, 'E': 4}.get(direction))
    while not robot.comp.outputs:
        robot.comp.tick() 
    return robot.comp.outputs.pop()

# Main      
f = open('assets/15.txt', 'r')
intcode = [int(x) for x in f.read().rstrip().split(',')]

# Part 1
reverse = {'N': 'S','S': 'N','E': 'W','W': 'E'}
left = {'N': 'W','S': 'E','E': 'N','W': 'S'}
right = {'N': 'E','S': 'W','E': 'S','W': 'N'}

move = {
    'N': lambda robot: (robot.x, robot.y-1),
    'S': lambda robot: (robot.x, robot.y+1),
    'E': lambda robot: (robot.x+1, robot.y),
    'W': lambda robot: (robot.x-1, robot.y)
}
# curses init
stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE) # unkown
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK) # floor
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED) # wall
curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK) # bot 
curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK) # target
ccolors = {0: curses.color_pair(3), 1: curses.color_pair(2), 2: curses.color_pair(5), -1: curses.color_pair(1)}

robot = Robot(intcode[:])
maze = {}
moves = []
maze[(robot.x, robot.y)] = {'block': 1, 'possible': ['N', 'S', 'E', 'W']}

print_maze(stdscr)
found = None

while True:

# if (robot.x, robot.y) not in maze:
#     back = reverse.get(moves[-1]) if moves else None
#     possible = list(filter(lambda x: x is not back, ['N', 'S', 'E', 'W']))
#     maze[(robot.x, robot.y)] = {'back': back, 'possible': possible}

    move_dir = get_next_untried(maze[(robot.x, robot.y)]['possible'])


    if move_dir:
        maze[(robot.x, robot.y)]['possible'].remove(move_dir)

        next_block = int(explore_direction(move_dir))
        next_loc = move.get(move_dir)(robot)

        maze[next_loc] = {'block': next_block}
        # print_maze(stdscr)
        if next_block == 1 or next_block == 2:
            robot.x, robot.y = next_loc
            maze[next_loc]['possible'] = [x for x in ['N', 'S', 'E', 'W'] if x != reverse.get(move_dir)]
            moves.append(move_dir)
            if next_block == 2 and (found == None or found[1] < len(moves)):
                found = (next_loc, len(moves))
                stdscr.addstr(1, 0, f'Oxy found? {robot.x}, {robot.y}  {len(moves)}')

        # else: 
        
    else:
        if not moves:
            break
        move_dir = reverse[moves.pop()]
        next_block = int(explore_direction(move_dir))
        robot.x, robot.y = move.get(move_dir)(robot)

    # print_maze(stdscr)

curses.nocbreak()
curses.echo()
curses.endwin()

print(found)