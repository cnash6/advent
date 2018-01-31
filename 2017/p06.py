
def recurse(mem_blocks, i, val):
  mem_blocks[i] +=1
  if val > 1:
    return recurse(mem_blocks, (i+1) % len(mem_blocks), val-1)
  return mem_blocks

def do_it():
  mem_blocks = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
  # mem_blocks = [0,2,7,0]

  c = 0
  iters = []
  iters.append(mem_blocks[:])

  while(True):
    c+=1
    i = mem_blocks.index(max(mem_blocks))
    val = mem_blocks[i]
    mem_blocks[i] = 0
    mem_blocks = recurse(mem_blocks, (i+1) % len(mem_blocks), val)
    if mem_blocks in iters:
      return len(iters) - iters.index(mem_blocks)
      # return c # Problem 1
    iters.append(mem_blocks[:])

print(do_it())
