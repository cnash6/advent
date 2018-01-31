from p10 import knot
import binascii

puzzle_in = "oundnydw"
# puzzle_in = "flqrgnkx"

def print_grid(grid):
  for line in grid:
    print("".join(line))

def hex_to_bin(hex_in):
  astr = ""
  for character in list(hex_in):
    thing = int(character, 16)
    thing2 = format(thing, '0>4b')
    astr+=thing2
  return astr
  # return bin(int(hex_in, 16))[2:].zfill(len(hex_in))

# print(hex_to_bin("a0c2017"))


total = 0
grid = []
for x in range(128):
  hashed = knot(puzzle_in + "-" + str(x))
  bits = str(hex_to_bin(hashed))
  # bits = bits + "".join(["0" for x in range(128 - len(bits))])
  grid.append(list(bits))
  total += sum([int(x) for x in list(bits)])
print(total)

def explore_group(x, y, grid):
  grid[y][x] = "0"
  if 0 <= y+1 < len(grid) and 0 <= x < len(grid[y+1]) and int(grid[y+1][x]) == 1:
    grid = explore_group(x, y+1, grid)
  if 0 <= y < len(grid) and 0 <= x+1 < len(grid[y]) and int(grid[y][x+1]) == 1:
    grid = explore_group(x+1, y, grid)
  if 0 <= y-1 < len(grid) and 0 <= x < len(grid[y-1]) and int(grid[y-1][x]) == 1:
    grid = explore_group(x, y-1, grid)
  if 0 <= y < len(grid) and 0 <= x-1 < len(grid[y]) and int(grid[y][x-1]) == 1:
    grid = explore_group(x-1, y, grid)
  return grid

groups = 0 
for y in range(len(grid)):
  for x in range(len(grid[y])):
    # print((x,y))
    if(int(grid[y][x]) == 1):
      groups+=1
      grid = explore_group(x, y, grid)

print(groups)

