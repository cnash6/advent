f = open('assets/04.txt', 'r')
lines = [x.rstrip() for x in f.readlines()]

count = 0

for line in lines:
  words = line.split(" ")
  if len(words) == len(set(words)):
    count+=1

print(count)

count = 0

for line in lines:
  words = ["".join(sorted(x)) for x in line.split(" ")]
  if len(words) == len(set(words)):
    count+=1

print(count)

