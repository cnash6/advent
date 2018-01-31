def build_nodes(lines):
  nodes = {}

  for line in lines:
    node = line.split(" <-> ")[0]
    connections = line.split(" <-> ")[1].split(", ")

    if node not in nodes:
      nodes[node] = []

    for connection in connections:
      if connection not in nodes[node]:
        nodes[node].append(connection)
      if connection not in nodes:
        nodes[connection] = []
      nodes[connection].append(node)

  return nodes

def count_connected_nodes(nodes, current, visited):
  visited.append(current)
  for node in nodes[current]:
    if node not in visited:
      count_connected_nodes(nodes, node, visited)
  return visited

f = open('assets/12.txt', 'r')
lines = [x.rstrip() for x in f.readlines()]

# lines = [
#   "0 <-> 2",
#   "1 <-> 1",
#   "2 <-> 0, 3, 4",
#   "3 <-> 2, 4",
#   "4 <-> 2, 3, 6",
#   "5 <-> 6",
#   "6 <-> 4, 5"
# ]

print(len(lines))

nodes = build_nodes(lines)

groups = []
for x in range(len(lines)):
  group = sorted(count_connected_nodes(nodes, str(x), []))
  if group not in groups:
    groups.append(group)

print(len(groups))



