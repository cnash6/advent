f = open('assets/06.txt', 'r')
lines = [x.rstrip() for x in f.readlines()]

# lines = [
#   "eedadn",
#   "drvtee",
#   "eandsr",
#   "raavrd",
#   "atevrs",
#   "tsrnev",
#   "sdttsa",
#   "rasrtv",
#   "nssdts",
#   "ntnada",
#   "svetve",
#   "tesnvt",
#   "vntsnd",
#   "vrdear",
#   "dvrsen",
#   "enarar"
# ]

chars = []
for i in range(len(lines[0])):
  chars.append({})

for line in lines:
  for char_i in range(len(line)):
    if line[char_i] in chars[char_i]:
      chars[char_i][line[char_i]]+=1
    else:
      chars[char_i][line[char_i]] = 1

print("".join([min(x, key=x.get) for x in chars]))
