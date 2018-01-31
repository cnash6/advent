def build_it(line):
  return {
    'p': line[0],
    'v': line[1],
    'a': line[2],
    'avg_a': 0
  }

f = open('assets/20.txt', 'r')
particles = [build_it([y.strip()[3:-1].split(',') for y in x.rstrip().split(', ')]) for x in f.readlines()]

the_min = {
  'avg_a': float('inf')
}

# i = 0
# for particle in particles:
#   particle['i'] = i
#   i+=1
#   a = particle['a']
#   particle['avg_a'] = (abs(int(a[0])) + abs(int(a[1])) + abs(int(a[2]))) / 3 
#   if particle['avg_a'] < the_min['avg_a']:
#     the_min = particle

for i in range(10000):
  print(i)
  print(len(particles))
  x = 0
  while x < len(particles):
    y = x+1
    removed = False
    while y < len(particles):
      if particles[x]['p'] == particles[y]['p']:
        removed = True
        print("collision at " + str(particles[x]['p']))
        particles.pop(y)
      else:
        y+=1
    if removed:
      particles.pop(x)
    x+=1

  for particle in particles:
    particle['v'][0] = int(particle['v'][0]) + int(particle['a'][0])
    particle['v'][1] = int(particle['v'][1]) + int(particle['a'][1])
    particle['v'][2] = int(particle['v'][2]) + int(particle['a'][2])

    particle['p'][0] = int(particle['p'][0]) + int(particle['v'][0])
    particle['p'][1] = int(particle['p'][1]) + int(particle['v'][1])
    particle['p'][2] = int(particle['p'][2]) + int(particle['v'][2])

  # input("Press Enter to continue...")


print(len(particles))

