
class Node:

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
    self.children = []

  def __str__(self):
    return "name: " + self.name + ", weight: " + str(self.weight) + ", children: " + str(len(self.children))

  def add_child(self, node):
    self.children.append(node)

  def get_weight(self):
    return self.weight + sum([x.get_weight() for x in self.children])

# ==============

def find_root():
  for line in lines:
    name = line.split(" (")[0]
    found = False
    for line2 in lines:
      if "->" in line2 and name in line2.split("-> ")[1]:
        found = True
        break
    if not found:
      return line

def build_node(line):
  if " -> " in line:
    s = line.split(" -> ")
  else:
    s = [line]
  name = s[0].split(" ")[0]
  weight = int(s[0].split(" ")[1][1:-1])
  node = Node(name, weight)

  if len(s) > 1:
    for child in s[1].split(", "):
      aline = list(filter(lambda x: child in x.split("(")[0], lines))
      if len(aline) > 0:
        node.add_child(build_node(aline[0]))
  return node

def are_children_balanced(node):
  if len(list(set([x.get_weight() for x in node.children]))) == 1:
    return node
  else: 
    weights = []
    for i in range(len(node.children)):
      weights.append(node.children[i].get_weight())
    found = -1
    for i in range(len(weights)):
      if weights[i] not in weights[:i] + weights[i+1:]:
        found = i
    print(weights)
    return are_children_balanced(node.children[found])

  # if len(node.children) == 0:
  #   return None
  # weights = []
  # for i in range(len(node.children)):
  #   weights.append(node.children[i].get_weight())
  # found = -1
  # for i in range(len(weights)):
  #   if weights[i] not in weights[:i] + weights[i+1:]:
  #     found = i
  # if found != -1:
  #   return node
  # else:
  #   return are_children_balanced(node.children[i])




f = open('assets/07.txt', 'r')
lines = [x.rstrip() for x in f.readlines()]
# lines = [
#   "pbga (66)",
#   "xhth (57)",
#   "ebii (61)",
#   "havc (66)",
#   "ktlj (57)",
#   "fwft (72) -> ktlj, cntj, xhth",
#   "qoyq (66)",
#   "padx (45) -> pbga, havc, qoyq",
#   "tknk (41) -> ugml, padx, fwft",
#   "jptl (61)",
#   "ugml (68) -> gyxo, ebii, jptl",
#   "gyxo (61)",
#   "cntj (57)"
# ]

root_line = find_root()
print("root: " + root_line)

root = build_node(root_line)

print(are_children_balanced(root))

# print(root.children[0].get_weight())
# print(root.children[1].get_weight())
# print(root.children[2].get_weight())











