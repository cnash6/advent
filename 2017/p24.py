# !/usr/bin/env python3
# [Part 1]
# 1423
# [Part 2]
# 1381


f = open('assets/24.txt', 'r')
components = [tuple(x.strip().split("/")) for x in f]
components = [(int(x[0]), int(x[1])) for x in components]
bridges = []
base = None

def sum_bridge(bridge):
  strength = 0
  for part in bridge:
      strength += part[0] + part[1]
  return strength

def build_bridges(bridge):
  last = bridge[-1][1]
  bridges = [bridge]
  for i in range(len(components)):
    if components[i] in bridge:
      continue
    if components[i][0] == last:
      bridges += build_bridges(bridge + [components[i]])
    elif components[i][1] == last:
      components[i] = tuple(reversed(components[i]))
      bridges += build_bridges(bridge + [components[i]])
  return bridges


for i in  range(len(components)):
  components[i] = tuple(sorted(list(components[i])))
  if components[i][0] == 0:
    base = components[i]
components.sort()
print(components)

bridges += build_bridges([base])
max_bridge = None
for b in bridges: 
  if max_bridge == None or sum_bridge(b) > sum_bridge(max_bridge):
    print(sum_bridge(b))
    max_bridge = b

print(b)
print(sum_bridge(b))



