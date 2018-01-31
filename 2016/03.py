f = open('assets/03.txt', 'r')
trips = f.readlines()
found = []
print(len(trips))

def is_triangle(nums):
  return nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[0]+nums[2]>nums[1]

for t in trips:
  nums = [int(x) for x in t.rstrip().split(',')];
  if(is_triangle(nums)):
    found.append(nums)
print(len(found))

new_trips = []

for i in range(len(trips)//3):
  t_0 = [int(x) for x in trips[i*3].rstrip().split(',')];
  t_1 = [int(x) for x in trips[(i*3)+1].rstrip().split(',')];
  t_2 = [int(x) for x in trips[(i*3)+2].rstrip().split(',')];

  print(t_0)
  new_trips.append([t_0[0], t_1[0], t_2[0]])
  new_trips.append([t_0[1], t_1[1], t_2[1]])
  new_trips.append([t_0[2], t_1[2], t_2[2]])

print(len(new_trips))

new_found = []
for t in new_trips:
  if(is_triangle(t)):
    new_found.append(t)

print(len(new_found))


