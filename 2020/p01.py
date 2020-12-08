#!/usr/bin/env python

from itertools import combinations # https://docs.python.org/3/library/itertools.html
from functools import reduce # https://docs.python.org/3/library/functools.html

# parameters:
    # input_file: name of the file to read
    # n: number of entries to search for and sum to the target value of 2020
def expenses(input_file, n): 
    # open the file in read mode
    f = open(input_file, 'r') 

    # List comprehension. Similar to a loop
    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    # basically: 
    #   for each element 'x' in the object 'f' 
    #   (in this case for each line in the file) 
    #   cast 'x' as an int
    expenses = [int(x) for x in f] 

    # for each combination of n expenses in the list of expenses (itertools rocks)
    # e.g. combinations([1,2,3], 2) => [(1,2), (2,3), (1,3)]
    for combination in combinations(expenses, n):
        # if the sum of the numbers in that combination == 2020
        if sum(combination) == 2020:
            # return the result of mapping them all together.
            # This line uses:
            #   reduce:
            #       reduce is one of the classic list functions in "map,
            #       filter, reduce". "Reduces" a list to one value by 
            #       multuplying each number against the previous result
            #   lambdas:
            #       lambdas are python's (relatively gross) way of implementing
            #       small, one-off functions that don't deserve to have their own 
            #       name. e,g, "lambda params: do something with params"  
            # 
            # Returning here allows us to "short circuit" and return once we find 
            # a solution and not check all the combinations. This becomes very useful
            # once the problems get harder
            return reduce(lambda x, y: x * y, list(combination))

# Part One
print(expenses('inputs/01.1', 2)) # 514579
print(expenses('inputs/01', 2))

# part Two
print(expenses('inputs/01.1', 3)) # 241861950
print(expenses('inputs/01', 3)) 