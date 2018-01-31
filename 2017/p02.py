f = open('assets/02.txt', 'r')
lines = [x.rstrip().split(',') for x in f.readlines()]


# 1

diffs = []
for line in lines:
  minnum = float('inf')
  maxnum = -1
  for num in line:
    if int(num) < minnum:
      minnum = int(num)
    if int(num) > maxnum:
      maxnum = int(num)
  diffs.append(maxnum-minnum)

print(sum(diffs))

# 2

# lines = [
#   ['5', '9', '2', '8'],
#   ['9', '4', '7', '3'],
#   ['3', '8', '6', '5']
# ]

divisors = []
print(len(lines))
for line in lines:
  s =  sorted([int(x) for x in line])
  s.reverse()
  print(s)
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      # print(s[i] + ":" + s[j])
      if int(s[i]) % int(s[j]) == 0:
        # print(s[i] + " / " + s[j] + " = " + str(int(s[i]) // int(s[j])))
        divisors.append(int(s[i]) // int(s[j]))

print(len(divisors))
print(divisors)
print(sum(divisors))

