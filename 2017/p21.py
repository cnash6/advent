
f = open('assets/21.txt', 'r')
rules_in = [x.strip() for x in f]

def rotate(sqgr): 
    return tuple(tuple(x) for x in zip(*sqgr[::-1]))

def collapse(tups):
  return "/".join(["".join(x) for x in tups])

def expand(line):
  return tuple([tuple(x) for x in line.split('/')])

if __name__ == '__main__':
  N = 18
  art=((".", "#", "."), (".", ".", "#"), ("#", "#", "#"))

  # print(collapse(art))

  rules = {}

  for r in rules_in:
    fro,to = [expand(x) for x in r.split(' => ')]

    orig = fro
    while True:
      rules[collapse(fro)] = collapse(to)
      fro = rotate(fro)
      if fro == orig:
        break

    fro = tuple(reversed(fro))

    orig = fro
    while True:
      rules[collapse(fro)] = collapse(to)
      fro = rotate(fro)
      if fro == orig:
        break

  # print(rules)

  for n in range(N):
    print(n)
    if len(art) % 2 == 0:
      d = 2
    else:
      d = 3
    new_art = []
    for i in range(len(art)//d):
      line = []
      for j in range(len(art)//d):
        sub = tuple([x[j*d:j*d+d] for x in art[i*d:i*d+d]])
        line.append(rules[collapse(sub)])
      new_art.append("/".join(["".join(y) for y in list(zip(*[x.split("/") for x in line]))]))
    art = expand("/".join(new_art))

  print(collapse(art).count('#'))

  

