#!/usr/bin/env python3

# steps = [3, 4, 1, 5]
# rope = [x for x in range(5)]

# unhashed = "1,2,3"

def knot(unhashed):  
  rope = [x for x in range(256)]
  addendum = [17, 31, 73, 47, 23]

  steps = []
  for c in unhashed:
    steps.append(ord(c))
  steps = steps+addendum

  skip = 0
  i = 0

  for z in range(64):
    for step in steps:
      sub = []
      for x in range(step):
        sub.append(rope[(i+x)%len(rope)])
      sub = sub[::-1]
      for x in range(step):
        rope[(i+x)%len(rope)] = sub[x]
      i = (i+step)%len(rope) + skip
      skip+=1

  final = []
  for x in range(16):
    sub = rope[x*16:(x*16)+16]
    sub_str = str(sub[0]) + " ^ " + str(sub[1]) + " ^ " + str(sub[2]) + " ^ " + str(sub[3]) + " ^ " + str(sub[4]) + " ^ " + str(sub[5]) + " ^ " + str(sub[6]) + " ^ " + str(sub[7]) + " ^ " + str(sub[8]) + " ^ " + str(sub[9]) + " ^ " + str(sub[10]) + " ^ " + str(sub[11]) + " ^ " + str(sub[12]) + " ^ " + str(sub[13]) + " ^ " + str(sub[14]) + " ^ " + str(sub[15])
    res = str(hex(int(eval(sub_str)))[2:])
    final.append(res if len(res) == 2 else "0"+res)

  return "".join(final)

# unhashed = "187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"
# print(knot(unhashed))