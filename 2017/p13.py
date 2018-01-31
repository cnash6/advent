def run_through(delay, layers, upper_limit):
  for step in range(upper_limit): 
    if step in layers:
      layer_range = layers[step]
      if (step+1+delay) % ((layer_range-1)*2) == 1:
        return False
  return True

f = open('assets/13.txt', 'r')
layers = {int(k): int(v) for k, v in [x.rstrip().split(": ") for x in f.readlines()]} # Create dict of vals

upper_limit = max(layers, key=int)+1 # Get max layer number

delay = 0
while True:
  if(run_through(delay, layers, upper_limit)):
    print(delay)
    break
  else:
    delay+=1

