f = open('assets/09.txt', 'r')
data = [x.rstrip() for x in f.read()]
# data = "<{o\"i!a,<{i<a>"

i = 0
depth = 0
garbage = False
score = 0
gargabe_chars = 0
while i < len(data):
  c = data[i]

  if c == '!':
    i+=1
  elif c == '>':
    garbage = False
  else:
    if not garbage:
      if c == '{':
        depth +=1
      elif c == '}':
        score+=depth
        depth-=1
      elif c == '<':
        garbage = True
    else:
      gargabe_chars+=1
  i+=1

print(score)
print(gargabe_chars)


