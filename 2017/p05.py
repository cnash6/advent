f = open('assets/05.txt', 'r')
lines = [int(x.rstrip()) for x in f.readlines()]

# lines = [0, 3, 0, 1, -3]

c = 0
i = 0 
searching = True
while(searching):
  v = lines[i]
  c+=1
  if i+v >= 0 and i+v < len(lines):
    if lines[i] >= 3:
      lines[i]-=1
    else:
      lines[i]+=1
    i+=v
  else:
    searching = False

print(c)