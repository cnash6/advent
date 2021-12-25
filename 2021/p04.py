#!/usr/bin/env python

from utils import *

def mark_board(board, n):
    for y in range(len(board)):
        board[y] = ['X' if x==n else x for x in board[y]]

    for row in board:
        if all([x=='X' for x in row]):
            return board, True

    for x in range(len(board[0])):
        if all(row[x]=='X' for row in board):
            return board, True
    
    return board, False 

def calc_bingo(board, n):
    return sum(int(n) for n in [x for y in board for x in y] if n!='X') * int(n)

def do_it(inputs):
    numbers = inputs[0].split(',')
    boards = [[[z for z in y.split(' ') if z] for y in inputs[i*6+2:i*6+7]] for i in range(len(inputs)//6)]
    for n in numbers:
        new_boards = []
        for board in boards: 
            b, bingo = mark_board(board, n)
            if bingo:
                print(f'bingo! {calc_bingo(b, n)}')
            else:
                new_boards.append(b)
        boards = new_boards
        if not boards:
            return "done"
    return "no_bingo"

print(do_it(aocin("inputs/04.1")))
print(do_it(aocin("inputs/04")))
