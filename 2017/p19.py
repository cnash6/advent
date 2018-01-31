import copy

f = open('assets/19.txt', 'r')
amap = [[y for y in x.rstrip()] for x in f.readlines()]
for line in amap:
  print("".join(line))

def move_it(state):
  steps, x, y, d, amap, word = state['steps'], state['x'], state['y'], state['d'], state['amap'], state['word']
  steps+=1
  # print("######")
  # print(x,y)
  # print(d)

  # thing = copy.deepcopy(amap)
  # thing[y][x] = '?'
  # for line in thing:
  #   print("".join(line))


  x_1, y_1 = x,y
  if d == 'n':
    y_1-=1
  if d == 's':
    y_1+=1
  if d == 'e':
    x_1+=1
  if d == 'w':
    x_1 -=1

  # print(x_1, y_1)

  if amap[y_1][x_1] == '+':
    if 0 <= y_1-1 < len(amap) and 0 <= x_1 < len(amap[y_1-1]) and (amap[y_1-1][x_1] == '|' or amap[y_1-1][x_1].isalpha()) and d not in ['n','s']:
      d = 'n'
    elif 0 <= y_1+1 < len(amap) and 0 <= x_1 < len(amap[y_1+1]) and (amap[y_1+1][x_1] == '|' or amap[y_1+1][x_1].isalpha())and d not in ['n','s']:
      d = 's'
    elif 0 <= x_1+1 < len(amap[y_1]) and 0 <= x_1+1 < len(amap[y_1]) and (amap[y_1][x_1+1] == '-' or amap[y_1][x_1+1].isalpha()) and d not in ['e','w']:
      d = 'e'
    elif 0 <= x_1-1 < len(amap[y_1]) and 0 <= x_1-1 < len(amap[y_1]) and (amap[y_1][x_1-1] == '-' or amap[y_1][x_1-1].isalpha()) and d not in ['e','w']:
      d = 'w'
  elif amap[y_1][x_1].isalpha():
    word = word + amap[y_1][x_1]
    if (d == 'n' and amap[y_1-1][x_1] not in ['+','|','-']) or (d == 's' and amap[y_1+1][x_1] not in ['+','|','-']) or (d == 'e' and amap[y_1][x_1+1] not in ['+','|','-']) or (d == 'w' and amap[y_1][x_1-1] not in ['+','|','-']):
      print(word)
      print(steps)
      return word
  
  state = {
    'steps': steps,
    'x': x_1,
    'y': y_1,
    'd': d,
    'amap': amap,
    'word': word
    } 
  return state




if __name__ == '__main__':
  x,y = 0,0

  for i in range(len(amap[0])):
    if amap[0][i] == '|':
      x = i 
      break

  state = {
    'steps': 0,
    'x': x,
    'y': y,
    'd': 's',
    'amap': amap,
    'word': ''
  }

  while True:
    state = move_it(state)
    if isinstance(state, str):
      break
    # input("Press Enter to continue...")



