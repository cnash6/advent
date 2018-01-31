f = open('assets/11.txt', 'r')
steps = f.read().rstrip().split(',')

# steps = ["ne","ne","s","s"]
x = 0 
y = 0
z = 0
max_steps = 0

for step in steps:
  if step == 'n':
    y+=1
    z-=1
  if step == 'ne':
    x+=1
    z-=1
  if step == 'nw':
    x-=1
    y+=1
  if step == 's':
    y-=1
    z+=1
  if step == 'se':
    x+=1
    y-=1
  if step == 'sw':
    x-=1
    z+=1
  if max(abs(x),abs(y),abs(z)) > max_steps:
    max_steps = max(abs(x),abs(y),abs(z)) 

print(max(abs(x),abs(y),abs(z)))
print(max_steps)