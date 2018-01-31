f = open('assets/07.txt', 'r')
lines = [x.rstrip() for x in f.readlines()]

# lines = [
#   "abba[mnop]qrst",
#   "abcd[bddb]xyyx",
#   "aaaa[qwer]tyui",
#   "ioxxoj[asdfgh]zxcvbn"
# ]

count = 0

for line in lines:
  good = True
  line_good = False
  for i in range(len(line)):
    if line[i] == "[":
      good = False
    elif line == "]":
      good = True
    else:
      if good and i+3 < len(line) and line[i:i+2] == (line[i+2:i+4])[::-1] and line[i] != line[i+1]:
        line_good = True
  if line_good:
    print(line)
    count+=1 

print(count)